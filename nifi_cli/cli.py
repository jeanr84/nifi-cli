import click
from halo import Halo
from prompt_toolkit import prompt
from prompt_toolkit.history import InMemoryHistory

from .completer import NifiCompleter


@click.command()
@click.option('--host', prompt='NiFi host')
@click.option('--port', default=8080)
def cli(host, port):
    history = InMemoryHistory()

    with Halo(text='Trying to connect to {}:{}'.format(host, port), spinner='earth') as spinner:
        import time

        time.sleep(1)

        spinner.text = 'Fetching API'

        time.sleep(1)

        spinner.succeed('Connected')

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
