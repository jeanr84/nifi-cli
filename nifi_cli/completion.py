import re
from bs4 import BeautifulSoup
import urllib.request


class NifiCompletion:


    def __init__(self, host, port):
        self.host = host
        self.port = port

    def get_html_content(self):
        URL = "http://" + self.host + ":" + str(self.port)

        REST_API_PAGE = URL + "/nifi-docs/rest-api/index.html"

        html = urllib.request.urlopen(REST_API_PAGE).read()
        return BeautifulSoup(html, "html.parser")

    def create_tree(self):
        tree = {}
        p = re.compile("{.*}")

        html_content = self.get_html_content()

        for html_endpoint in html_content.findAll("div", {"class": "endpoints"}):
            endpoint = html_endpoint.find("span", {"class": "path hidden"}).string
            methods = map((lambda x: x.string.lower()), html_endpoint.findAll("div", {"class": "method"}))
            current_tree = tree
            parts = endpoint[1:].split('/')
            for part in parts:
                if not p.match(part):
                    if part not in current_tree:
                        current_tree[part] = {}
                    current_tree = current_tree[part]
            for method in methods:
                current_tree[method] = None

        return tree
