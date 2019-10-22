import requests

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
    print(result.json())


def correct_start():
    print('Correct /api/start use:')

    result = requests.post('{}/api/start'.format(base_url),
                           data={
                                'user': 'jbshep',
                                'project': 'laketech',
                                'label': 'bugfix',
                           })
    print(result.json())


def correct_stop():
    print('Correct /api/stop use:')

    result = requests.post('{}/api/stop'.format(base_url),
                           data={
                                'user': 'jbshep',
                                'project': 'laketech',
                                'label': 'enhancement',
                           })
    r = result.json()
    print(r)
    print('error is:', r['type'])
    

bogus_init()
print('--------------')
correct_init()
print('--------------')
correct_start()
print('--------------')
correct_stop()
