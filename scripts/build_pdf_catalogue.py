"""Generate the PDF catalogue, or use --check to verify the maintained page.

Run from any directory with Python 3.11 or later. The metadata and original
files stay unchanged; only pdfs.md is written when --check is not supplied.
"""
import argparse
from html import escape
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def catalogue_text():
    """Render the catalogue in the source order without duplicating PDF assets."""
    metadata = json.loads((ROOT / '_static/original-pdfs.json').read_text(encoding='utf-8'))
    lines = [
        '# Published PDFs', '',
        'Download the complete parts, individual sections, and examples below. '
        f'Section numbers and update dates follow the [JCSS PDF catalogue]({metadata["catalogue_url"]}). '
        'These files retain their original contents and may differ from the online chapters.', '',
    ]
    current_group = None
    for record in metadata['files']:
        if record['group'] != current_group:
            current_group = record['group']
            lines.extend(['', f'## {current_group}', '',
                          '| Section | Document | Catalogue update |',
                          '| --- | --- | --- |'])
        # A plain HTML link uses the existing static copy. A MyST download role
        # would make a second copy under Sphinx's hashed _downloads directory.
        filename = Path(record['file']).name
        link = (f'<a href="{escape(record["file"], quote=True)}" '
                f'download="{escape(filename, quote=True)}">'
                f'{escape(record["title"])} (PDF)</a>')
        lines.append(f'| {record["section"] or "—"} | {link} | {record["date"]} |')
    return '\n'.join(lines) + '\n'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    arguments = parser.parse_args()
    page = ROOT / 'pdfs.md'
    text = catalogue_text()
    if arguments.check:
        if not page.is_file() or page.read_text(encoding='utf-8') != text:
            raise SystemExit('PDF catalogue is stale. Run scripts/build_pdf_catalogue.py.')
        print('PDF catalogue agrees with the file metadata.')
    else:
        page.write_text(text, encoding='utf-8')
        print('Updated pdfs.md.')


if __name__ == '__main__':
    main()
