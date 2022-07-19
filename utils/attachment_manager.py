import json

import allure
from requests import Response


def attach_response(response: Response):
    allure.attach(
        f'{response.request.method} {response.request.url}\n\n'
        f'Headers\n {response.request.headers}\n\n'
        f'Body\n {response.request.body}',
        'Request',
        allure.attachment_type.TEXT
    )
    allure.attach(
        f'Status code{response.status_code}\n\n'
        f'Headers\n {response.headers}\n\n'
        f'Body\n {response.json()}',
        'Response',
        allure.attachment_type.TEXT
    )


def attach_dictionary(name: str, dictionary: dict):
    allure.attach(
        json.dumps(dictionary, indent=4),
        name,
        allure.attachment_type.JSON
    )


def attach_json(name: str, schema: str):
    allure.attach(
        json.dumps(schema, indent=4),
        name,
        allure.attachment_type.JSON
    )
