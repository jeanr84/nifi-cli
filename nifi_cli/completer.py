from prompt_toolkit.completion import Completer, Completion

from .completion import tree


class NifiCompleter(Completer):
    def get_completions(self, document, complete_event):
        text = document.text

        current_tree = tree
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
