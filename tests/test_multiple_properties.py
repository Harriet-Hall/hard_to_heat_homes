from app.main.epc_api import epc_api_call
from dotenv import load_dotenv
import os 

load_dotenv()

TOKEN = os.getenv('EPC_ENCODED_API_TOKEN')

BASE_URL = 'https://epc.opendatacommunities.org/api/v1/domestic/search?'
HEADERS = {
        'Accept': 'application/json',
        'Authorization': f'Basic {TOKEN}'
    }


def test_returns_two_properties():
    array_of_properties = epc_api_call(HEADERS, {'local-authority' :'E09000008', 'size' : '2'})['rows']
    assert len(array_of_properties) == 2