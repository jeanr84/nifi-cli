from prompt_toolkit import prompt
from prompt_toolkit.history import InMemoryHistory

from .completer import NifiCompleter


def cli():
    history = InMemoryHistory()

    cmd = ""
    while cmd != 'exit':
        try:
            cmd = prompt("> ", completer=NifiCompleter(), history=history)
            print('You entered:', cmd)
        except KeyboardInterrupt:
            continue  # Control-C pressed. Try again.
        except EOFError:
            break  # Control-D pressed.

    print('Bye!')