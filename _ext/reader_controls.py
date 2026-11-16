"""Connect published PDF references to the existing book download menu."""
import json
from pathlib import Path
from urllib.parse import urlsplit

from sphinx.errors import ExtensionError


def load_pdf_links(app):
    """Read the maintained mapping once per build and reject invalid targets."""
    source = Path(app.srcdir)
    mapping = json.loads((source / '_static/original-pdfs.json').read_text(encoding='utf-8'))
    for page, record in mapping['chapters'].items():
        if not (source / (page + '.md')).is_file():
            raise ExtensionError(f'PDF mapping refers to an unknown chapter: {page}')
        destination = urlsplit(record['url'])
        if (destination.scheme != 'https' or destination.netloc != 'www.jcss-lc.org'
                or not destination.path.lower().endswith('.pdf')):
            raise ExtensionError(f'Expected an official JCSS PDF URL for {page}')
    app.pmc_pdf_links = mapping


def add_download_context(app, pagename, templatename, context, doctree):
    """Separate the published PDF, Markdown source, and browser print actions."""
    context['pmc_original'] = app.pmc_pdf_links['chapters'].get(pagename)
    context['pmc_pdf_catalogue'] = app.pmc_pdf_links['catalogue_url']
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
