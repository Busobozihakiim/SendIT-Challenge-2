"""CONFIG FOR TESTING ENDPOINTS"""
import pytest
from app import create_app

EMPTY_ORDER = {}

DELIVERY = {"pick_up":"ntinda",            
            "drop_off":"bukoto",
            "parcel_name":"Sofa",
            "description":"L shaped brown sofa",            
            "user_id": "mary"
            }

MISSING_KEYS = {
                "drop_off":"bukoto",
                "parcel_name":"Sofa",
                "description":"L shaped brown sofa",                
                "user_id": "mary"
                }

EMPTY_FIELDS = {"pick_up":"",                
                "drop_off":"bukoto",
                "parcel_name":"Sofa",
                "description":"L shaped brown sofa",                
                "user_id": "mary"
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
