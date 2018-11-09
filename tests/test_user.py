"""TESTING ENDPOINTS"""
import unittest
from app import create_app

EMPTY_ORDER = {}

DELIVERY = {"pick_up":"ntinda",
            "recepient":"John Abrahms",
            "drop_off":"bukoto",
            "parcel_name":"Sofa",
            "description":"L shaped brown sofa",
            "weight":"5kgs"
            }

MISSING_KEYS = {"recepient":"John Abrahms",
                "drop_off":"bukoto",
                "parcel_name":"Sofa",
                "description":"L shaped brown sofa",
                "weight":"5kgs"
                }

EMPTY_FIELDS = {"pick_up":"",
                "recepient":"John Abrahms",
                "drop_off":"bukoto",
                "parcel_name":"Sofa",
                "description":"L shaped brown sofa",
                "weight":"5kgs"
               }

class Testuser(unittest.TestCase):
    """Class for unit tests"""

    def setUp(self):
        self.app = create_app('test')
        self.app = self.app.test_client()

    def test_delivery_order_with_no_data(self):
        """Test whether the user has submitted an empty post"""
        with self.app.post('api/v1/parcels', json=EMPTY_ORDER) as current:
            assert current.status_code == 400
            assert 'You entered nothing' in str(current.json)

    def test_delivery_oder_with_missing_values(self):
        """test whether the user has submitted a post with missing values"""
        with self.app.post('api/v1/parcels', json=EMPTY_FIELDS) as current:
            assert current.status_code == 400

    def test_delivery_order_with_missing_keys(self):
        """test whether the user is missing some fields"""
        with self.app.post('api/v1/parcels', json=MISSING_KEYS) as current:
            assert current.status_code == 400
            assert 'You are missing a required field' in str(current.json)

    def test_make_order(self):
        """Test to create a delivery order """
        with self.app.post('api/v1/parcels', json=DELIVERY) as current:
            assert current.status_code == 201
            assert 'Delivery order created'in str(current.json)
