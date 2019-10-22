'''
Here is sample code you can use in your client-side program
to communicate with the Flask server via HTTP.  It uses
the well-known Python requests library, which you can
retrieve using 'pip install requests'.

Your 'tracker init --remote url' command will receive and
store the 'key' for a project.
Then, your tracker client will send the key as the BasicAuth
username (no password) with each start/stop request.

Below, I've also shown how to decode the response from each
HTTP request.
'''

import requests
from requests.auth import HTTPBasicAuth

base_url = 'http://localhost:5000'

def bogus_init():
    print('Intentional /api/init error:')
    result = requests.post('{}/api/init'.format(base_url),
                           data={
                                'user': 'jbshep',
                                #'project': 'laketech',
                           })
    print(result)


def correct_init():
    print('Correct /api/init use:')

    result = requests.post('{}/api/init'.format(base_url),
                           data={
                                'user': 'jbshep',
                                'project': 'laketech',
                           })
    r = result.json()
    print(r)
    return r['key']


def bogus_start_no_key():
    print('Bogus /api/start, missing BasicAuth user key')

    result = requests.post('{}/api/start'.format(base_url),
                           #auth=HTTPBasicAuth('commented out',''),
                           data={
                                'user': 'jbshep',
                                'label': 'bugfix',
                           })
    print(result)
    

def correct_start(key):
    print('Correct /api/start use:')

    result = requests.post('{}/api/start'.format(base_url),
                           auth=HTTPBasicAuth(key,''),
                           data={
                                'user': 'jbshep',
                                'label': 'bugfix',
                           })
    print(result.json())


def correct_stop(key):
    print('Correct /api/stop use:')

    result = requests.post('{}/api/stop'.format(base_url),
                           auth=HTTPBasicAuth(key,''),
                           data={
                                'user': 'jbshep',
                                'label': 'enhancement',
                           })
    r = result.json()
    print(r)
    print('error is:', r['type'])
    

bogus_init()
print('--------------')
key = correct_init()
print('--------------')
bogus_start_no_key()
print('--------------')
correct_start(key)
print('--------------')
correct_stop(key)
