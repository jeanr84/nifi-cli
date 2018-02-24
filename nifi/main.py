from prompt_toolkit import prompt
from prompt_toolkit.history import InMemoryHistory


def main():
    history = InMemoryHistory()

    cmd = ""
    while cmd != 'exit':
        try:
            cmd = prompt("> ", history=history)
            print('You entered:', cmd)
        except EOFError:
            cmd = 'exit'
