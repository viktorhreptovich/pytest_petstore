from functools import wraps

import requests

from utils.attachment_manager import attach_response
from utils.request_result import RequestResult


class HttpManager:
    base_url = 'https://petstore.swagger.io'

    headers = {'accept': 'application/json',
               'Content-Type': 'application/json'}
    cookie = ""

    def attach(func):
        @wraps(func)
        def wrap(*func_args, **func_kwargs):
            result = func(*func_args, **func_kwargs)
            attach_response(result.response)
            return result

        return wrap

    @attach
    def get(self, url):
        result = requests.get(
            url=url,
            headers=HttpManager.headers,
            cookies=HttpManager.cookie
        )
        return RequestResult(result)

    @attach
    def post(self, url, body):
        result = requests.post(
            url=url,
            json=body,
            headers=HttpManager.headers,
            cookies=HttpManager.cookie
        )
        return RequestResult(result)

    @attach
    def put(self, url, body):
        result = requests.put(
            url=url,
            json=body,
            headers=HttpManager.headers,
            cookies=HttpManager.cookie
        )
        return RequestResult(result)

    @attach
    def delete(self, url):
        result = requests.delete(
            url=url,
            headers=HttpManager.headers,
            cookies=HttpManager.cookie
        )
        return RequestResult(result)
