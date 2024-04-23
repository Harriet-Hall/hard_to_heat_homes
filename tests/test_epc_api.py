import urllib.request
from urllib.parse import urlencode
import os
from dotenv import load_dotenv

load_dotenv()

QUERY_PARAMS = {'uprn':'200002791'}
BASE_URL = 'https://epc.opendatacommunities.org/api/v1/domestic/search?'

def epc_call():
    TOKEN = os.getenv('EPC_ENCODED_API_TOKEN')
    
    headers = {
        'Accept': 'application/json',
        'Authorization': f'Basic {TOKEN}'
    }

    encoded_params = urlencode(QUERY_PARAMS)
    full_url = f'{BASE_URL}{encoded_params}'

    with urllib.request.urlopen(urllib.request.Request(full_url, headers=headers)) as response:
        return response.status == 200
        

    return True

def test_200_response():
    assert epc_call() == True

# def test_not_200_response():
#     assert epc_call() == False