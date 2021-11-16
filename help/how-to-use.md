# How to Use

This guide gives an overview of how to install [jupyterbook](https://jupyterbook.org/intro.html) locally on your computer (for advanced users) as well as how to edit the PMC directly online without needing a local installation (recommended option).


## Local set-up

```{warning}
This setup is only recommended for advanced users who have basic knowledge of `git`, `python` and `markdown`.
```

### Installation

This chapter gives an introduction how to set-up and use jupyterbook on your local machine. Jupyterbook uses `python`, hence you need a local python environment to install jupyterbook.

In your local python environment install the following packages:

```
pip install jupyter-book matplotlib numpy
```

### Build command line interface

When you’ve written your book’s content, it is now time to build outputs for your book so that you may share them with others. For example, you may wish to build HTML files to host as a static website, or a PDF to share with colleagues.

he basic way to build your book is via the following command:

```
jupyter-book build <path-to-book>
```

For example if you in the book folder (i.e. where the `_config.yml` file is located) you shuld run:

```
jupyter-book build .
```

In the folder `_build`, you will find the created book.

## Online set-up

```{note}
The PMC was designed in such a way that editing, moderation and publication of the content can be carried out online without local installations of the required programmes.
```
### GitHub Account

To edit the PMC, you need a GitHub user account. If you don't have such an account yet, go to [github.com](https://github.com/) and click the sign up button. Please follow the instructions to create an account.

```{important}
During registration, you will be asked if you want to have a free or paid account. A free account is perfectly sufficient for editing the PMC!
```
After successful registration, you can use the functionalities of GitHub and edit the PMC online.


# Online editing

## First Steps
You also can edit the content of the [PMC online](https://jcss-pmc.github.io/PMC/part-00/intro.html), when you do not want to set-up jupyterbook on your local machine. Therefore a github account is needed (see XXX).

You have two options for online editing:

1. you can suggest changes to the text directly (`sugesst edits`), or
2. you can start a discussion on specific topics (`open issue`).


## Sugesst Edits

If you want to suggest direct changes to the text, you can do so using the `sugesst edits` function. To do this, go to the corresponding page of the PMC and move the mouse over the ![GitHubLogo](https://fr.wikipedia.org/wiki/GitHub#/media/Fichier:Octicons-mark-github.svg) button.  In the menu below, you can select option `sugesst edits`. Click on this option.

```{image} images/edit-online.png
:height: 200px
:name: image-edit-online
```




## Open Issues
