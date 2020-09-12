import sys
import fire
from donno import notes


class App:
    def add(self):
        '''Add a new note in the current notebook'''
        notes.add_note()

    def a(self):
        """Alias of add command"""
        self.add()

    def delete(self, no):
        notes.delete_note(no)

    def list(self, number):
        '''List most updated <number> notes'''
        print(notes.list_notes(number))

    def l(self, number):  # noqa
        """Alias of list command"""
        self.list(number)

    def edit(self, no):
        notes.update_note(no)

    def e(self, no):
        '''Alias of edit command'''
        self.edit(no)

    def search(self, *keys):
        if len(keys) == 0:
            sys.exit('Add at least 1 keyword to search')

        path_list = notes.simple_search(keys)
        if len(path_list) == 0:
            sys.exit("No match found")
        else:
            print(notes.note_list(path_list))

    def s(self, *keys):
        '''alias for search command'''
        self.search(*keys)

    def view(self, no):
        notes.view_notes(no)

    def v(self, no):
        '''Alias of view command'''
        self.view(no)


if __name__ == '__main__':
    fire.Fire(App)
