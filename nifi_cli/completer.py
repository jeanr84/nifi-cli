from prompt_toolkit.completion import Completer, Completion


class NifiCompleter(Completer):

    def __init__(self, tree):
        self.tree = tree

    def get_completions(self, document, complete_event):
        text = document.text

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
