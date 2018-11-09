"""TESTING ENDPOINTS"""
from .conftest import  EMPTY_FIELDS, EMPTY_ORDER, MISSING_KEYS, DELIVERY

def test_delivery_order_with_no_data(set_up_client):
    """Test whether the user has submitted an empty post"""
    response = set_up_client.post('api/v1/parcels', json=EMPTY_ORDER)
    assert response.status_code == 400
    assert 'You entered nothing' in str(response.json)

def test_delivery_oder_with_missing_values(set_up_client):
    """test whether the user has submitted a post with missing values"""
    response = set_up_client.post('api/v1/parcels', json=EMPTY_FIELDS)
    assert response.status_code == 400

def test_delivery_order_with_missing_keys(set_up_client):
    """test whether the user is missing some fields"""
    response = set_up_client.post('api/v1/parcels', json=MISSING_KEYS)
    assert response.status_code == 400
    assert 'You are missing a required field' in str(response.json)

def test_make_order(set_up_client):
    """Test to create a delivery order """
    response = set_up_client.post('api/v1/parcels', json=DELIVERY)
    assert response.status_code == 201
    assert 'Delivery order created'in str(response.json)

def test_see_all_order(set_up_client):
    """test to see all orders"""
    response = set_up_client.get('api/v1/parcels')
    assert response.status_code == 200
