import urllib.request
from urllib.parse import urlencode
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('EPC_ENCODED_API_TOKEN')

QUERY_PARAMS = {'uprn':'200002791'}
BASE_URL = 'https://epc.opendatacommunities.org/api/v1/domestic/search?'
HEADERS = {
        'Accept': 'application/json',
        'Authorization': f'Basic {TOKEN}'
    }

def epc_call(headers, params):
    
    
  

    encoded_params = urlencode(params)
    full_url = f'{BASE_URL}{encoded_params}'
    try:
        with urllib.request.urlopen(urllib.request.Request(full_url, headers=headers)) as response:
            return response.status == 200
    except Exception:
        return False
            
        

   

def test_200_response():
    assert epc_call(HEADERS, QUERY_PARAMS) == True

def test_not_200_response():
    assert epc_call({}, QUERY_PARAMS) == False