# How to Use

This is a short guid how to set-up and work with [jupyterbook](https://jupyterbook.org/intro.html).

## Set-up

### Installation

This chapter gives an introduction how to set-up and use jupyterbook on your local machine. Jupyterbook uses python, hence you need a local python environment to install jupyterbook.

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

## Online

You also can edit the content online, when you do not want to set-up jupyterbook on your local machine.

Therefore, go to the online version of the book and click at the top button `sugesst edits`. An online text editor will open up where you can make your changes. 


```{image} images/edit-online.png
:height: 200px
:name: image-edit-online
```

