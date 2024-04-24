import urllib.request
from urllib.parse import urlencode
import os
from dotenv import load_dotenv
from dummy_data import dummy_data
import json

load_dotenv()

TOKEN = os.getenv('EPC_ENCODED_API_TOKEN')

QUERY_PARAMS = {'uprn':'200002791'}
BASE_URL = 'https://epc.opendatacommunities.org/api/v1/domestic/search?'
HEADERS = {
        'Accept': 'application/json',
        'Authorization': f'Basic {TOKEN}'
    }

def epc_api_call(headers, params):

    encoded_params = urlencode(params)
    full_url = f'{BASE_URL}{encoded_params}'

    try:
        with urllib.request.urlopen(urllib.request.Request(full_url, headers=headers)) as response:
            response_body = response.read()

            if len(response_body) > 0:
                return json.loads(response_body)
            else: return {}
    except Exception:
        return False
            

def test_200_response():
    assert type(epc_api_call(HEADERS, QUERY_PARAMS)) is dict

def test_200_response_invalid_uprn():
    assert epc_api_call(HEADERS, {'uprn' : '123456789'}) == {}


def test_not_200_response():
    assert epc_api_call({}, QUERY_PARAMS) == False

def test_result_is_JSON():
    assert epc_api_call(HEADERS, QUERY_PARAMS) == dummy_data