from prompt_toolkit.completion import Completer, Completion
from nifi_cli.completion import NifiCompletion


class NifiCompleter(Completer):

    def __init__(self):
        self.tree = NifiCompletion().create_tree()

    def get_completions(self, document, complete_event):
        text = document.text

        # TODO : do this only at the beginning
        current_tree = self.tree
        words = text.split('.')

        for index, part in enumerate(words):
            if index == len(words) - 1:
                for w in current_tree:
                    if w.startswith(part):
                        yield Completion(w, -len(part))
            else:
                if part in current_tree:
                    current_tree = current_tree[part]
                else:
                    current_tree = {}
