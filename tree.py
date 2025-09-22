#!/usr/bin/env python3

'''
It prints the current directory's tree structure, like the tree command.

It is useful when the system doesn't have that command available.

References:
https://en.wikipedia.org/wiki/Box-drawing_characters
https://www.w3.org/TR/xml-entity-names/025.html

'''

from os import scandir as sd

def print_directory_tree(path, prefix=""):
    '''Recursively prints the directory tree structure.'''
    
    entry_prefix = "├── "
    nested_prefix = "│   "

    for entry in sd(path):
        entry_string = f'{prefix}{entry_prefix}{entry.name}'
        nested_string = f'{prefix}{nested_prefix}'
        if entry.is_dir():
            print(entry_string)
            print_directory_tree(entry.path, nested_string)
        else:
            print(entry_string)

if __name__ == "__main__":
    start_path = "." # Start with the current directory
    print_directory_tree(start_path)

