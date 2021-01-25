# Introduction

Parse the structural definition of the exported files created by note-taking applicaitons.

donno import notes exported by these applications by the definitions defined here.

# Joplin

The metadata of JSON file exported by Joplin:

type 1: note
  'title': title
  'body': contents
  'user_created_time'
  'user_updated_time'
  'parent_id': 'id' of its parent notebook

type 2: notebook
  'title': name of the notebook
  'user_created_time'
  'user_updated_time'
  'parent_id': 'id' of its parent notebook

type 3: None

type 4: resource, image or file
  'id': in the contents of a note, e.g.:'![7f2c066aefc29dbf2872fbfea74dfdfa.png](:/d1459b610d2e4784adb607e3dfd6b59b)\r\n'
  'title': filename of the resource

type 5: tag
  'title': name of tag

type 6: relation between note and tag
  'note_id'
  'tag_id'

