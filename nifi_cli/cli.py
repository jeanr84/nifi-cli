import click
from halo import Halo
from prompt_toolkit import prompt
from prompt_toolkit.history import InMemoryHistory

from .completer import NifiCompleter
from nifi_cli.completion import NifiCompletion
import urllib.request


@click.command()
@click.option('--host', prompt='NiFi host')
@click.option('--port', default=8080)
def cli(host, port):
    history = InMemoryHistory()

    with Halo(text='Trying to connect to {}:{}'.format(host, port), spinner='earth') as spinner:
        spinner.text = 'Fetching API'
        try:
            nifi_completer = NifiCompleter(NifiCompletion(host, port).create_tree())
            spinner.succeed('Connected')
        except urllib.error.URLError:
            print("\nConnexion refused, make sure that the Nifi server is running")
            exit()

    cmd = ""
    while cmd != 'exit':
        try:
            cmd = prompt("> ", completer=nifi_completer, history=history)
            print('You entered:', cmd)
        except KeyboardInterrupt:
            continue  # Control-C pressed. Try again.
        except EOFError:
            break  # Control-D pressed.

    print('Bye!')
