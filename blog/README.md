# Publish Notes to Blog

You can publish notes in a specified notebook (default: *Tech*,
change it with `don conf set blog.notebook NewNotebookName`) to your blog.

Under the hood, notes (markdown files) is converted to static web pages
(HTML files) with pandoc, then pushed to an user-specified
*static website hosting platform*, such as [GitHub Pages](https://pages.github.com/).

When the *autopublish* option is on, every time you backup notes to remote *note*
repository, the blog is updated accordingly.
Thus we get the benefits of both worlds:
high efficiency of console note-taking apps and easy sharing and community-interactivity
of cloud-based ones, without sync notes repository to blog repository manually.

## Basic Setup

Copy a default web page template to config folder:
```
cp blog/homepage.html ~/.config/donno
cp blog/note.html ~/.config/donno
cp blog/blog.css ~/.config/donno
```

## Configurations

* blog.autopublish: on/off, default: off
* blog.notebook: default: Tech
