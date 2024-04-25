from dummy_data import dummy_data

class Property():
    def __init__(self, uprn):
        self.uprn = uprn

def test_property_has_uprn():
    dummy_property = Property('200002791')
    assert dummy_property.uprn == '200002791'



