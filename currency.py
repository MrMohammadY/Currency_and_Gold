import requests
import json
from config import URL_CURRENCY, rules


def get_data_curr():
    """
    get a data of url and return json data
    :return:
    """
    response = requests.get(URL_CURRENCY)
    data = json.loads(response.content)
    return data


def create_data_curr(data):
    """
    get currency of json data and
    get 3 time(timestamp,time update data,time current) of json data
    :param data: get json data
    :return: list of currency & timestamp & last update & now time
    """
    currency_data = data['list']
    timestamp = data["timeCurrent"][1]
    time_update = data['timeUpdate'][1]
    time_current = f'{data["timeCurrent"][1]} {data["timeCurrent"][2]}'
    list_currency = list()

    for cu in currency_data:
        if cu['nameFa'] in rules['currency']['which_currency']:
            list_currency.append(cu)

    return list_currency, timestamp, time_update, time_current


def create_data_file_curr(curr, timestamp):
    """
    make archive of currency
    :param curr: currency
    :param timestamp: timestamp like: 1 ابان 99
    :return:
    """
    with open(f'archive_currency/{timestamp}.json', 'w') as f:
        f.write(json.dumps(curr))
