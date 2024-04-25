from dummy_data import dummy_data
from app.main.epc_api import epc_api_call
import os 
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('EPC_ENCODED_API_TOKEN')
QUERY_PARAMS = {'uprn':'200002791'}
HEADERS = {
        'Accept': 'application/json',
        'Authorization': f'Basic {TOKEN}'
    }

class Property():
    def __init__(self, uprn):
        self.uprn = uprn

def test_property_has_uprn():
    dummy_property = Property('200002791')
    assert dummy_property.uprn == '200002791'

def test_property_has_uprn_from_dummy_data():
    dummy_property = Property(dummy_data['rows'][0]['uprn'])
    assert dummy_property.uprn == '200002791'

def test_property_has_uprn_from_api_call():
    dummy_property = Property(epc_api_call(HEADERS, QUERY_PARAMS)['rows'][0]['uprn'])
    assert dummy_property.uprn == '200002791'


