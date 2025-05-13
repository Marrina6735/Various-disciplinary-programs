import json

from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk


def read_json(path) -> dict | list[dict]:
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def create_index(agent: Elasticsearch, index_name: str, settings: dict):
    agent.indices.create(index=index_name, body=settings)


def upload(index, data):
    for i, item in enumerate(data):
        print(f'Обработка {i+1} из {len(data)}')
        yield {
            '_index': index,
            '_source': item
        }


def main():
    login = 'jinr_school_17'
    password = 'dJ7Z4zGD'
    index = 'jobhunt_17'
    url = 'https://pluton.mephi.ru/elk-e'
    es = Elasticsearch(
        url,
        basic_auth=(login, password)
    )

    print(es.info())
    #  settings = read_json('mapping.json')
    #  create_index(es, index, settings)
    data = read_json('data.json')
    bulk(es, upload(index, data))


if __name__ == "__main__":
    main()
