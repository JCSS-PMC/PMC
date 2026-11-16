"""Connect published PDF references to the existing book download menu."""
import hashlib
import json
from pathlib import Path
import posixpath

from sphinx.errors import ExtensionError


def load_pdf_links(app):
    """Read the maintained mapping once per build and reject invalid targets."""
    source = Path(app.srcdir)
    mapping = json.loads((source / '_static/original-pdfs.json').read_text(encoding='utf-8'))
    files = {}
    pdf_directory = (source / '_static/pdfs').resolve()
    for record in mapping['files']:
        path = (source / record['file']).resolve()
        if not path.is_relative_to(pdf_directory) or path.suffix.lower() != '.pdf':
            raise ExtensionError(f'Expected a file inside _static/pdfs: {record["file"]}')
        if not path.is_file():
            raise ExtensionError(f'Missing published PDF: {record["file"]}')
        if (path.stat().st_size != record['bytes']
                or hashlib.sha256(path.read_bytes()).hexdigest() != record['sha256']):
            raise ExtensionError(f'Published PDF differs from its source record: {record["file"]}')
        if record['source_url'] in files:
            raise ExtensionError(f'Duplicate PDF source: {record["source_url"]}')
        files[record['source_url']] = record
    for page, record in mapping['chapters'].items():
        if not (source / (page + '.md')).is_file():
            raise ExtensionError(f'PDF mapping refers to an unknown chapter: {page}')
        if record['url'] not in files:
            raise ExtensionError(f'No local PDF for chapter: {page}')
    app.pmc_pdf_links = mapping
    app.pmc_pdf_files = files


def add_download_context(app, pagename, templatename, context, doctree):
    """Separate the published PDF, Markdown source, and browser print actions."""
    original = app.pmc_pdf_links['chapters'].get(pagename)
    context['pmc_original'] = None
    if original:
        file = app.pmc_pdf_files[original['url']]['file']
        context['pmc_original'] = {
            **original,
            'url': posixpath.relpath(file, posixpath.dirname(pagename) or '.'),
            'filename': Path(file).name,
        }
    context['pmc_pdf_catalogue'] = app.builder.get_relative_uri(pagename, 'pdfs')
    for group in context.get('header_buttons', []):
        if group.get('label') != 'download-buttons':
            continue
        for button in group['buttons']:
            if button.get('label') == 'download-pdf-button':
                button['text'] = 'Print this page'
            elif button.get('label') == 'download-source-button':
                button['text'] = 'Markdown source'


def omit_execution_scripts(app, pagename, templatename, context, doctree):
    """Omit unused Thebe bootstrap from this static, non-executing reader."""
    scripts = []
    for script in context.get('script_files', []):
        filename = str(getattr(script, 'filename', script))
        body = str(getattr(script, 'attributes', {}).get('body', ''))
        if 'sphinx-thebe.js' not in filename and 'THEBE_JS_URL' not in body:
            scripts.append(script)
    context['script_files'] = scripts


def setup(app):
    app.connect('builder-inited', load_pdf_links)
    # Run after the book theme has assembled its standard header buttons.
    app.connect('html-page-context', add_download_context, priority=900)
    app.connect('html-page-context', omit_execution_scripts, priority=900)
    return {'version': '1.0', 'parallel_read_safe': True, 'parallel_write_safe': True}
