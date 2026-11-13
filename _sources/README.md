# JCSS Probabilistic Model Code

The **Probabilistic Model Code (PMC)** is developed by the [Joint Committee on Structural Safety (JCSS)](https://www.jcss-lc.org/). It provides a basis for probabilistic modelling and reliability assessment in the design of new structures and the assessment of existing structures. This repository contains the Markdown sources, figures, and references used to build the online book with Jupyter Book.

## Read the PMC

1. [Online book](https://jcss-pmc.github.io/PMC/part-00/intro.html): browse the chapters and their references.
2. [Published PDFs](https://www.jcss-lc.org/jcss-probabilistic-model-code/): download the published parts and individual sections, with their listed update dates.
3. [JCSS website](https://www.jcss-lc.org/): information about JCSS, its activities, and other publications.

## Contents

| Part | Subject | Source directory |
| --- | --- | --- |
| I | Basis of Design | `part-01/` |
| II | Load Models | `part-02/` |
| III | Resistance Models | `part-03/` |

## Cite the PMC

Cite the part or chapter consulted and use its own publication or update date. For an online chapter, include the access date because its content can change. The following examples use JCSS as the institutional author.

1. **Published PDF section**

   Joint Committee on Structural Safety (JCSS). (2026). *Environmental Exposure for Reinforced Concrete*. Probabilistic Model Code, Part II: Load Models, Section 2.21. Updated November 2026. [PDF](https://www.jcss-lc.org/wp-content/uploads/2026/11/jcss-pmc-2026-11-environmental-exposure-for-reinforced-concrete.pdf).

2. **Online chapter**

   Joint Committee on Structural Safety (JCSS). (2026). *Environmental Exposure for Reinforced Concrete*. Probabilistic Model Code, Part II: Load Models, Chapter 23. Updated November 2026. Accessed 13 November 2026. [Online chapter](https://jcss-pmc.github.io/PMC/part-02/environmental-exposure-for-reinforced-concrete.html).

Use the numbering shown in the version consulted: this chapter is Section 2.21 in the published PDF and Chapter 23 in the online book. Replace the example's access date with the date of your own consultation.

## Contribute

The [editing guide](help/how-to-use.md) explains how to propose changes through GitHub.

1. **Report an error or propose a change** through [Issues](https://github.com/JCSS-PMC/PMC/issues). Identify the chapter, the relevant passage or equation, and any supporting references.
2. **Suggest an edit** using the online book's GitHub menu or by editing a fork of this repository. Submit a pull request against `JCSS-PMC/PMC:master` for the maintainers to review.
3. **Check the rendered result** when changing text, equations, figures, or references. Keep each pull request focused and explain the reason for the change.

Each chapter carries an `Updated: MM.YYYY` line below its title. The date records the latest substantive content revision accepted by the editors. Follow the [update-date convention](help/how-to-use.md#chapter-update-dates) when proposing a revision, and keep corresponding HTML and PDF versions consistent.

## Build locally

<details>
<summary>Repository structure and build instructions</summary>

The introduction is in `part-00/` and the editing guide is in `help/`. Chapter order is defined in [`_toc.yml`](_toc.yml), book settings in [`_config.yml`](_config.yml), and bibliographic references in [`references.bib`](references.bib).

Install Python 3.11, as used by the repository's build workflow, and download or clone this repository. Create and activate a Python virtual environment before installing the dependencies from [`requirements.txt`](requirements.txt), which specifies Jupyter Book 1.x. From the repository root, run:

```sh
python -m pip install -r requirements.txt
jupyter-book build .
```

Open `_build/html/index.html` to inspect the generated book. To preview it through a local web server, run:

```sh
python -m http.server 8000 --bind 127.0.0.1 --directory _build/html
```

Then open `http://127.0.0.1:8000/` in your browser. Generated files are written to `_build/` and are excluded from version control. The existing [GitHub Actions workflow](.github/workflows/book.yml) builds and publishes the online book when changes are pushed to `master`.

</details>
