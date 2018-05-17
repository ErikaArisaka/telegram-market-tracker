from ebaysdk.finding import Connection as Finding
from ebaysdk.exception import ConnectionError

keyword = input()

try:
    api = Finding(config_file='config.py')
    response = api.execute('findItemsAdvanced', {'keywords': keyword})
    results = response.dict()
    items = results['searchResult']['item']
    for item in items:
        print(item)
except ConnectionError as e:
    print(e)
    print(e.response.dict())