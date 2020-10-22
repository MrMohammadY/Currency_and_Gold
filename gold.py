import requests
import json
from config import URL_GOLD, rules


def get_data_go():
    """
    get a data of url and return json data
    :return:
    """
    response = requests.get(URL_GOLD)
    data = json.loads(response.content)
    return data


def create_data_go(data):
    """
    get gold of json data and
    get 3 time(timestamp,time update data,time current) of json data
    :param data: get json data
    :return: list of gold & timestamp & last update & now time
    """
    gold_data = data['list']
    timestamp = data["timeCurrent"][1]
    time_update = data['timeUpdate'][1]
    time_current = f'{data["timeCurrent"][1]} {data["timeCurrent"][2]}'
    list_gold = list()

    for g in gold_data:
        if g['name'] in rules['gold']['which_gold']:
            list_gold.append(g)

    return list_gold, timestamp, time_update, time_current


def create_data_file_go(go, timestamp):
    """
    make archive of currency
    :param go: gold
    :param timestamp: timestamp like: 1 ابان 99
    :return:
    """
    with open(f'archive_gold/{timestamp}.json', 'w') as f:
        f.write(json.dumps(go))
