import re
from bs4 import BeautifulSoup
import urllib.request


class NifiCompletion:

    def get_html_content(self):
        # TODO : Make the hostname and port configurable
        URL = "http://localhost:8080"
        REST_API_PAGE = URL + "/nifi-docs/rest-api/index.html"

        html = urllib.request.urlopen(REST_API_PAGE).read()
        return BeautifulSoup(html, "html.parser")

    def create_tree(self):
        tree = {}
        p = re.compile("{.*}")

        try:
            html_content = self.get_html_content()
        except urllib.error.URLError:
            return {}

        for html_endpoint in html_content.findAll("div", {"class": "endpoints"}):
            # TODO : Fix the "path hidden" part which ignore some endpoints (ex : labels)
            endpoint = html_endpoint.find("span", {"class": "path hidden"}).string
            method = html_endpoint.find("div", {"class": "method"}).string.lower()
            current_tree = tree
            parts = endpoint[1:].split('/')
            for part in parts:
                if not p.match(part):
                    if part not in current_tree:
                        current_tree[part] = {}
                    current_tree = current_tree[part]
            current_tree[method] = None

        return tree
