import requests
import json
from config import URL_GOLD, rules


def get_data():
    response = requests.get(URL_GOLD)
    data = json.loads(response.content)
    return data


def create_data(data):
    gold_data = data['list']
    timestamp = data["timeCurrent"][1]
    time_update = data['timeUpdate'][1]
    time_current = f'{data["timeCurrent"][1]} {data["timeCurrent"][2]}'
    list_gold = list()
    print(timestamp)

    for g in gold_data:
        if g['name'] in rules['gold']['which_gold']:
            list_gold.append(g)

    return list_gold, timestamp, time_update, time_current


def create_data_file(go, timestamp):
    with open(f'archive_gold/{timestamp}.json', 'w') as f:
        f.write(json.dumps(go))


gold = create_data(get_data())
create_data_file(gold[0], gold[1])
