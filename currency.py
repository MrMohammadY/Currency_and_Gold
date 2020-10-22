import requests
import json
from config import URL_CURRENCY, rules


def get_data():
    response = requests.get(URL_CURRENCY)
    data = json.loads(response.content)
    return data


def create_data(data):
    currency_data = data['list']
    timestamp = data["timeCurrent"][1]
    time_update = data['timeUpdate'][1]
    time_current = f'{data["timeCurrent"][1]} {data["timeCurrent"][2]}'
    list_currency = list()

    for cu in currency_data:
        if cu['nameFa'] in rules['currency']['which_currency']:
            list_currency.append(cu)

    return list_currency, timestamp, time_update, time_current


def create_data_file(curr, timestamp):
    with open(f'archive_currency/{timestamp}.json', 'w') as f:
        f.write(json.dumps(curr))


currency = create_data(get_data())
create_data_file(currency[0], currency[1])
