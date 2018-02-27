from bs4 import BeautifulSoup
import urllib.request

class Completion:

    REST_API_URL = "http://localhost:8080/nifi-docs/rest-api/index.html"

    html =  urllib.request.urlopen(REST_API_URL).read()
    soup = BeautifulSoup(html, "html.parser")



    tree = {'flowfile-queues': {'listing-requests': {'get': {}, 'post': {}}, 'drop-requests': {'get': {}, 'post': {}},
                            'flowfiles': {'get': {}, 'content': {'get': {}}}}, 'counters': {'get': {}, 'put': {}},
        'policies': {'get': {}, 'post': {}}, 'funnels': {'get': {}},
        'tenants': {'search-results': {'get': {}}, 'user-groups': {'get': {}, 'post': {}},
                    'users': {'get': {}, 'post': {}}},
        'versions': {'active-requests': {'put': {}, 'post': {}}, 'process-groups': {'post': {}},
                     'revert-requests': {'get': {}, 'process-groups': {'post': {}}},
                     'update-requests': {'get': {}, 'process-groups': {'post': {}}}}, 'output-ports': {'get': {}},
        'remote-process-groups': {'get': {}, 'output-ports': {'put': {}}, 'input-ports': {'put': {}}},
        'controller-services': {'get': {}, 'state': {'get': {}, 'clear-requests': {'post': {}}},
                                'references': {'get': {}}, 'descriptors': {'get': {}}},
        'system-diagnostics': {'get': {}}, 'input-ports': {'get': {}}, 'snippets': {'put': {}, 'post': {}},
        'controller': {'registry-clients': {'get': {}, 'post': {}}, 'history': {'delete': {}},
                       'reporting-tasks': {'post': {}}, 'bulletin': {'post': {}}, 'controller-services': {'post': {}},
                       'config': {'get': {}}, 'cluster': {'get': {}, 'nodes': {'get': {}}}},
        'flow': {'config': {'get': {}}, 'reporting-task-types': {'get': {}}, 'output-ports': {'status': {'get': {}}},
                 'remote-process-groups': {'status': {'get': {}, 'history': {'get': {}}}},
                 'processor-types': {'get': {}}, 'client-id': {'get': {}}, 'input-ports': {'status': {'get': {}}},
                 'about': {'get': {}}, 'controller': {'controller-services': {'get': {}}, 'bulletins': {'get': {}}},
                 'registries': {'get': {}, 'buckets': {'flows': {'get': {}, 'versions': {'get': {}}}, 'get': {}}},
                 'templates': {'get': {}}, 'current-user': {'get': {}}, 'search-results': {'get': {}},
                 'banners': {'get': {}}, 'history': {'get': {}, 'components': {'get': {}}},
                 'cluster': {'search-results': {'get': {}}, 'summary': {'get': {}}}, 'prioritizers': {'get': {}},
                 'status': {'get': {}}, 'process-groups': {'get': {}, 'controller-services': {'get': {}},
                                                           'status': {'get': {}, 'history': {'get': {}}}},
                 'reporting-tasks': {'get': {}}, 'processors': {'status': {'get': {}, 'history': {'get': {}}}},
                 'controller-service-types': {'get': {}}, 'bulletin-board': {'get': {}},
                 'connections': {'status': {'get': {}, 'history': {'get': {}}}}},
        'templates': {'delete': {}, 'download': {'get': {}}}, 'data-transfer': {'transactions': {'post': {}},
                                                                                'output-ports': {'transactions': {
                                                                                    'flow-files': {'get': {}},
                                                                                    'put': {}}}, 'input-ports': {
            'transactions': {'flow-files': {'post': {}}, 'put': {}}}},
        'site-to-site': {'get': {}, 'peers': {'get': {}}}, 'resources': {'get': {}},
        'process-groups': {'get': {}, 'variable-registry': {'get': {}, 'update-requests': {'get': {}, 'post': {}}},
                           'templates': {'import': {'post': {}}, 'upload': {'post': {}}, 'post': {}},
                           'local-modifications': {'get': {}}, 'funnels': {'post': {}}, 'output-ports': {'post': {}},
                           'remote-process-groups': {'post': {}}, 'process-groups': {'post': {}},
                           'template-instance': {'post': {}}, 'input-ports': {'post': {}},
                           'snippet-instance': {'post': {}}, 'processors': {'post': {}},
                           'controller-services': {'post': {}}, 'labels': {'post': {}}, 'connections': {'post': {}}},
        'provenance': {'get': {}, 'lineage': {'get': {}, 'post': {}}, 'search-options': {'get': {}}, 'post': {}},
        'reporting-tasks': {'get': {}, 'state': {'get': {}, 'clear-requests': {'post': {}}},
                            'descriptors': {'get': {}}},
        'processors': {'get': {}, 'state': {'get': {}, 'clear-requests': {'post': {}}}, 'descriptors': {'get': {}}},
        'labels': {'get': {}}, 'provenance-events': {'get': {}, 'replays': {'post': {}},
                                                     'content': {'input': {'get': {}}, 'output': {'get': {}}}},
        'connections': {'get': {}}, 'access': {'download-token': {'post': {}}, 'get': {},
                                               'oidc': {'exchange': {'post': {}}, 'callback': {'get': {}},
                                                        'request': {'get': {}}}, 'kerberos': {'post': {}},
                                               'knox': {'callback': {'get': {}}, 'request': {'get': {}}},
                                               'ui-extension-token': {'post': {}}, 'token': {'post': {}},
                                               'config': {'get': {}}}}
