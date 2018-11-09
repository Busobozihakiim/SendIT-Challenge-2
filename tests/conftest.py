"""CONFIG FOR TESTING ENDPOINTS"""
import pytest
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

@pytest.fixture(scope='module')
def set_up_client():
    """create new app that will be used for a test"""
    #creating new flask app and a test client
    app = create_app('test')
    client = app.test_client()

    #creating the application context and
    #allowing test functions to run by calling test client
    #and finally cleaning house
    ctx = app.app_context()
    ctx.push()
    yield client
    ctx.pop()
