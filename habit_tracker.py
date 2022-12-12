import requests, os
from datetime import datetime


#initialize global variables
USERNAME = os.getenv('PIXELA_USER')
TOKEN = os.getenv('PIXELA_TOKEN')
GRAPH_NAME = 'coding'
PIXELA_ENDPOINT = 'https://pixe.la/v1/users'
GRAPH_ENDPOINT = f'{PIXELA_ENDPOINT}/{USERNAME}/graphs'
VALUE_ENDPOINT = f'{GRAPH_ENDPOINT}/{GRAPH_NAME}'
#create user relevant
USER_PARAMS = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}
#create graph relevant
GRAPH_CONFIG = {
    'id': 'coding',
    'name': 'Coding',
    'unit': 'Hours',
    'type': 'float',
    'color': 'sora',
}
HEADERS = {
    'X-USER-TOKEN': TOKEN,
}
CONT = True


def create_user():
    '''Create a user on Pixela.'''
    os.system('clear')
    user_params = '\n'.join(f'{key}: {value}' for key, value in USER_PARAMS.items())
    choice = input(f'{user_params}\nUse current USER_PARAMS? "y"\n ~ ').lower()
    if choice == 'y':
        response = requests.post(url=PIXELA_ENDPOINT, json=USER_PARAMS)
        print(response.text)
    else:
        uname = input('Username:\n ~ ')
        pw = input('Token/Password:\n ~ ')
        temp = {
            'token': uname,
            'username': pw,
            'agreeTermsOfService': 'yes',
            'notMinor': 'yes',
        }
        response = requests.post(url=PIXELA_ENDPOINT, json=temp)
        os.system('clear')
        print(f'Do not forget these:\nUsername: {uname}\nPassword: {pw}')
        print(response.text)


def create_graph():
    '''Create a graph on Pixela.'''
    os.system('clear')
    graph_config = '\n'.join(f'{key}: {value}' for key, value in GRAPH_CONFIG.items())
    choice = input(f'{USERNAME}\n{graph_config}\nUse pre-configured USERNAME and GRAPH_CONFIG? "y"\n ~ ').lower()
    if choice == 'y':
        response = requests.post(url=GRAPH_ENDPOINT, json=GRAPH_CONFIG, headers=HEADERS)
        print(response.text)
        print(f'Visit:\n{VALUE_ENDPOINT}.html')
    else:
        uname = input('Username:\n ~ ')
        os.system('clear')
        print('Name of graph.')
        id = input('id:\n ~ ')
        os.system('clear')
        print('coding, running, reading hours, etc.')
        name = input('name:\n ~ ')
        os.system('clear')
        print('hours, minutes, kilometers, miles, etc.')
        unit = input('unit:\n ~ ')
        os.system('clear')
        print('int, float, etc. ')
        type = input('type:\n ~ ')
        os.system('clear')
        print('shibafu (green), momiji (red), sora (blue), ichou (yellow), ajisai (purple) and kuro (black) are supported as color kind.')
        color = input('color: ~ ')
        temp = {
            'id': id,
            'name': name,
            'unit': unit,
            'type': type,
            'color': color,
        }
        graph_endpoint = f'{PIXELA_ENDPOINT}/{uname}/graphs'
        response = requests.post(url=graph_endpoint, json=temp, headers=HEADERS)
        print(response.text)
        print(f'Visit:\n{graph_endpoint}/{name}.html')


def add_pixel():
    '''Add a pixel to a Pixela graph.'''
    os.system('clear')
    today = datetime.now()
    value_endpoint = f'{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_NAME}'

    choice_1 = input(f'Username: {USERNAME}\nGraph name: {GRAPH_NAME}\nAre these correct "y"?\n ~ ')

    if choice_1 == 'y':
        pass
    else:
        uname = input('Username:\n ~ ')
        graph_name = input('Graph name:\n ~ ')
        value_endpoint = f'{PIXELA_ENDPOINT}/{uname}/graphs/{graph_name}'

    choice_2 = input('Add today "t" or add specific day "s"\n ~ ')
    
    if choice_2 == 't':
        quantity = input('Quantity to add:\n ~ ')
        add_today = {
            'date': today.strftime('%Y%m%d'),
            'quantity': quantity,
        }
        response = requests.post(url=value_endpoint, json=add_today, headers=HEADERS)
        print(response.text)
    else:
        year = int(input('Year:\n ~ ') )
        month = int(input('Month:\n ~ '))
        day = int(input('Day:\n ~ '))
        quantity = input('Quantity to add:\n ~ ')
        adjust_day = datetime(year=year, month=month, day=day)
        add_specific_day = {
            'date': adjust_day.strftime('%Y%m%d'),
            'quantity': quantity,
        }
        response = requests.post(url=value_endpoint, json=add_specific_day, headers=HEADERS)
        print(response.text)


def delete_pixel():
    '''Delete a pixel from a Pixela graph.'''
    os.system('clear')
    today = datetime.now().strftime("%Y%m%d")
    value_endpoint = f'{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_NAME}'

    choice_1 = input(f'Username: {USERNAME}\nGraph name: {GRAPH_NAME}\nAre these correct "y"?\n ~ ')

    if choice_1 == 'y':
        pass
    else:
        uname = input('Username:\n ~ ')
        graph_name = input('Graph name:\n ~ ')
        value_endpoint = f'{PIXELA_ENDPOINT}/{uname}/graphs/{graph_name}'

    choice_2 = input('Add today "t" or add specific day "s"\n ~ ')
    
    if choice_2 == 't':
        delete_endpoint = f'{value_endpoint}/{today}'
    else:
        year = int(input('Year:\n ~ ') )
        month = int(input('Month:\n ~ '))
        day = int(input('Day:\n ~ '))
        delete_day = datetime(year=year, month=month, day=day)
        delete_endpoint = f'{value_endpoint}/{delete_day.strftime("%Y%m%d")}'
    response = requests.delete(url=delete_endpoint, headers=HEADERS)
    print(response.text)


#start program functionality
try:
    os.system('clear')
    while CONT:
        choice = input('Would you like to:\n1. Create a user\n2. Create a graph\n3. Add a pixel\n4. Delete a pixel\n5. Exit\n ~ ').lower()

        match choice:
            case '1':
                create_user()
            case '2':
                create_graph()
            case '3':
                add_pixel()
            case '4':
                delete_pixel()
            case 'exit':
                CONT = False
            
except KeyboardInterrupt:
    print('\nSee you later.')