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

epc_test_property = epc_api_call(HEADERS, QUERY_PARAMS)['rows'][0]

class Property():
    def __init__(self, uprn, epc_rating):
        self.uprn = uprn
        self.epc_rating = epc_rating

def test_property_has_uprn():
    dummy_property = Property('200002791', None)
    assert dummy_property.uprn == '200002791'

def test_property_has_uprn_from_dummy_data():
    dummy_property = Property(dummy_data['rows'][0]['uprn'], None)
    assert dummy_property.uprn == '200002791'

def test_property_has_uprn_from_api_call():
    dummy_property = Property(epc_test_property['uprn'], None)
    assert dummy_property.uprn == '200002791'

def test_property_has_EPC_rating():
    dummy_property = Property('200002791', 'D')
    assert dummy_property.epc_rating == 'D'
    



