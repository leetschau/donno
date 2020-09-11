# Donno

A simple note-take CLI application.    

## Usage

```
don a        # add a new note
don l        # list existing notes
don s nim thunder    # search notes contains "nim" and "thunder"
don e 3      # edit note #3 in note list or searching results
don del 3    # delete note #3 in note list or searching results
don b        # backup notes to remote repository
don r        # restore notes from remote repository
don p 3      # preview note #3 in browser
don s compile -n nim -t config  # search notes which "nim" in its title, "config" in tags and "compile" in contents
don s -r "[nim|thunder]"  # search notes contains "nim" or "thunder"
don pub      # publish notes to blog
```

## Configuration

File path: ~/.config/donno/donno.conf

### General

* editor: which editor to use to create/update note, default: `nvim`
* notebook: current notebook name, no default value
* base_dir: root folder of donno data files, default: ~/.donno
* vimrc_home: when editor is vim or neovim, the configuration home folder, default: ~/.config/nvim
* resource_dir: folder name (in base_dir) to store attachments of notes, default: resources

### Blog

* url: blog url
* publish_cmd: command to publish note to blog

## Roadmap

1. Basic note-taking functions: add, delete, list, search, view, update notes

1. Configuration module: see [Configuration](#configuration);

1. Support adding attachments into notes, espeicially images

1. Preview: render markdown notes to HTML and previewed in browser

1. Synchronize notes between hosts (based on VCS, such as git)

1. Import/Export from/to other open source note-taking apps, such as [Joplin]()

1. Advanced search function: search by title, tag, notebook and content

1. Search with regular expression;

1. Basic publishing module: publish to blog, such as github.io

1. Advanced publishing function: publish specific note, or notes in specific notebook

