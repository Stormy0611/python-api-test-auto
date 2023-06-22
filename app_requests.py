import pytest
from pytest_steps import test_steps
from jsonschema import validate
import json
import requests
from dotenv import load_dotenv
import os

load_dotenv()
ROOT_URL = os.getenv('ROOT')


def send_req(method='get', endpoint="/", headers={}, params={}, data={}):

    url = ROOT_URL + endpoint

    session = requests.session()
    response = session.request(method=method, url=url, headers=headers, params=params, data=data)

    return response


class TestAPI:

    @test_steps(
        'test_api'
    )
    def test_api(self):
        res_data =send_req()
        assert (res_data.status_code == 200), f"Status Code validation failed for {res_data.request.url}"
        assert validate(res_data.json(), get_weather_data_schema), \
            f"Schema Validation failed for {res_data.request.url}"
        assert (res_data.json()['name'] == 'Pune')
        yield