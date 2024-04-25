from dummy_data import dummy_data

class Property():
    def __init__(self, uprn):
        self.uprn = uprn

def test_property_has_uprn():
    dummy_property = Property('200002791')
    assert dummy_property.uprn == '200002791'

def test_property_has_uprn_from_dummy_data():
    dummy_property = Property(dummy_data['rows'][0]['uprn'])
    assert dummy_property.uprn == '200002791'

