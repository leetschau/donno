from typing import List
from functools import reduce
from datetime import datetime
from pathlib import Path
import subprocess
import os
import sh

BASE_DIR = Path.home() / ".donno"
REPO = BASE_DIR / 'repo'
NOTE_FILES = REPO.glob('*.md')
EDITOR = 'nvim'
EDITOR_CONF = {'XDG_CONFIG_HOME': '$HOME/Documents/sources/vimrcs/text'}
CURRENT_NB = '/Diary/2020'

TEMP_FILE = 'newnote.md'
REC_FILE = BASE_DIR / 'record'


def add_note():
    now = datetime.now()
    created = now.strftime("%Y-%m-%d %H:%M:%S")
    current_nb = CURRENT_NB
    header = ('Title: \nTags: \n'
              f'Notebook: {current_nb}\n'
              f'Created: {created}\n'
              f'Updated: {created}\n\n------\n\n')
    with open(TEMP_FILE, 'w') as f:
        f.write(header)
    subprocess.run([EDITOR, TEMP_FILE], env={**os.environ, **EDITOR_CONF})
    # EDITOR_CONF must be put AFTER `os.environ`, for in above syntax,
    # the latter will update the former
    # meanwhile, sh package is not suitable for TUI, so here I use subprocess
    fn = f'note{now.strftime("%y%m%d%H%M%S")}.md'
    print(f'Save note to {REPO}/{fn}')
    if not REPO.exists():
        REPO.mkdir(parents=True)
    sh.mv(TEMP_FILE, REPO / fn)


def extract_header(path: Path) -> str:
    header_line_number = 5
    with open(path) as f:
        header = [next(f).strip().split(': ')[1]
                  for x in range(header_line_number)]
    return (f'[{header[3][2:]}] {header[0]} [{header[1]}] {header[2]} '
            f'{header[3]}')


def record_to_details():
    title_line = 'No. Updated, Title, Tags, Notebook, Created'
    with open(REC_FILE) as f:
        paths = [line.strip() for line in f.readlines()]
    headers = [extract_header(path) for path in paths]
    with_index = [f'{idx + 1}. {ele}' for idx, ele in enumerate(headers)]
    return '\n'.join([title_line, *with_index])


def list_notes(number: int):
    file_list = sorted(NOTE_FILES, key=lambda f: f.stat().st_mtime,
                       reverse=True)
    with open(REC_FILE, 'w') as f:
        f.write('\n'.join([str(path) for path in file_list[:number]]))
    return record_to_details()


def delete_note(no):
    pass


def filter_word(file_list: List[str], word: str) -> List[str]:
    if len(file_list) == 0:
        return []
    return sh.grep('-i', '-l', word, file_list).stdout.decode(
            'UTF-8').strip().split('\n')


def simple_search(word_list: List[str]) -> List[str]:
    search_res = reduce(filter_word, word_list, list(NOTE_FILES))
    with open(REC_FILE, 'w') as f:
        f.write('\n'.join([str(path) for path in search_res]))
    return record_to_details()


def note_list(file_list: List[str]) -> str:
    return file_list
