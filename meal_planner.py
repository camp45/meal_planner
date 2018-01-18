import requests
import json


def getheaders():
    with open('headers.json', 'r') as f:
        return json.loads(f.read())

def updatelist(grocery_items):
    for i in grocery_items:
        payload = {}
        url = 'https://a.wunderlist.com/api/v1/tasks'
        payload['list_id'] = 268337594
        payload['title'] = i
        r = requests.post(url, data=json.dumps(payload), headers=getheaders())
        if r.status_code != 201:
            print('Adding ' + i + ' to list failed.')


def main():
    grocery_items = ['Eggs', 'Bread', 'Milk', 'Cheese']
    updatelist(grocery_items)


if __name__ == '__main__':
    main()