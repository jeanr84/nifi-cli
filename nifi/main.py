from prompt_toolkit import prompt
from prompt_toolkit.history import InMemoryHistory


def main():
    history = InMemoryHistory()

    cmd=""
    while cmd != 'exit':
        cmd = prompt("> ", history=history)
        print('You entered:', cmd)
