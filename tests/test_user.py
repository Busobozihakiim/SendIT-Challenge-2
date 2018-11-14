"""TESTING ENDPOINTS"""
import json
from .conftest import  EMPTY_FIELDS, EMPTY_ORDER, MISSING_KEYS, DELIVERY
def test_change_location(set_up_client):
    """Change location of delivery order when none has been made"""
    response = set_up_client.put('api/v1/admin/2/ntinda/change', content_type='application/json')
    assert response.status_code == 200
    assert 'You have no delivery orders' in str(response.json)

def test_get_all_orders_by_userid(set_up_client):
    """test to see all orders when none exist"""
    reponss = set_up_client.get('api/v1/users/mary/parcels')
    assert reponss.status_code == 200
    assert 'You have not made any delivery orders' in  str(reponss.json)

def test_see_order_by_ids(set_up_client):
    """test to see an order by its id"""
    #testing when you dont have delivery orders
    reponss = set_up_client.get('api/v1/parcels/1')
    assert reponss.status_code == 200
    assert 'No deliveries made yet' in  str(reponss.json)

def test_cancel_delivery_order_with_no_order(set_up_client):
    """cancel a delivery order"""
    response = set_up_client.put('api/v1/parcels/3/cancel', content_type='application/json')
    assert response.status_code == 200
    assert 'You have no delivery orders' in str(response.json)

def test_see_all_order(set_up_client):
    """test to see all orders"""
    response = set_up_client.get('api/v1/parcels', content_type='application/json')
    assert response.status_code == 200
    assert 'You dont have any delivery orders' in str(response.json)

def test_delivery_order_with_no_data(set_up_client):
    """Test whether the user has submitted an empty post"""
    response = set_up_client.post('api/v1/parcels', data=json.dumps(EMPTY_ORDER), content_type='application/json')
    assert response.status_code == 400
    assert b'You entered nothing' in response.data

def test_delivery_oder_with_missing_values(set_up_client):
    """test whether the user has submitted a post with missing values"""
    response = set_up_client.post('api/v1/parcels',  data=json.dumps(EMPTY_FIELDS), content_type='application/json')
    assert response.status_code == 400
    assert b'You are missing pick_up in your input' in response.data

def test_delivery_order_with_missing_keys(set_up_client):
    """test whether the user is missing some fields"""
    response = set_up_client.post('api/v1/parcels',  data=json.dumps(MISSING_KEYS), content_type='application/json')
    assert response.status_code == 400
    assert 'You are missing a required field' in str(response.json)

def test_make_order(set_up_client):
    """Test to create a delivery order """
    response = set_up_client.post('api/v1/parcels', data=json.dumps(DELIVERY), content_type='application/json')
    assert response.status_code == 201
    assert 'Delivery order created'in str(response.json)

def test_see_orders_with_data(set_up_client):
    """test to see all orders with orders"""
    respons = set_up_client.post('api/v1/parcels',  data=json.dumps(DELIVERY), content_type='application/json')
    assert 'Delivery order created'in str(respons.json)
    response = set_up_client.get('api/v1/parcels')
    assert response.status_code == 200
    assert 'Available Delivery Orders' in str(response.json)

def test_see_order_by_id(set_up_client):
    """test to see an order by its id"""
    #testing when the id exists
    id_exists = set_up_client.get('api/v1/parcels/1')
    assert id_exists.status_code == 200
    assert "Here is the delivery order of id 1" in str(id_exists.json)
    #testing when the id doesnt exist
    id_no_exist = set_up_client.get('api/v1/parcels/5')
    assert id_no_exist.status_code == 200
    assert "this delivery order of id 5 doesnt exist" in str(id_no_exist.json)

def test_get_all_orders_by_userid_withdata(set_up_client):
    """test to get all delivery orders by a specific userid"""
    #testing with a known user id
    using_userid = set_up_client.get('api/v1/users/mary/parcels')
    assert using_userid.status_code == 200
    #testing when the user id is non existant
    no_user_id = set_up_client.get('api/v1/users/fisher/parcels')
    assert no_user_id.status_code == 200
    assert 'The user fisher doesnt have parcels and doesnt exist' in str(no_user_id.json)

def test_cancel_delivery_order_with_order(set_up_client):
    """cancel a delivery order"""
    #testing with a delivery order in place
    response = set_up_client.post('api/v1/parcels',  data=json.dumps(DELIVERY), content_type='application/json')
    assert response.status_code == 201
    resp = set_up_client.put('api/v1/parcels/1/cancel')
    assert resp.status_code == 200
    assert 'delivery order has been canceled' in str(resp.json)
    response = set_up_client.put('api/v1/parcels/8/cancel', content_type='application/json')
    assert response.status_code == 200
    assert 'Delivery order 8 not found' in str(response.json)

def test_change_location_with_order(set_up_client):
    """Change location of delivery order when an order exits"""
    respond = set_up_client.post('api/v1/parcels',  data=json.dumps(DELIVERY), content_type='application/json')
    assert respond.status_code == 201
    response = set_up_client.put('api/v1/admin/1/ntinda/change', content_type='application/json')
    assert response.status_code == 200
    assert 'current location has been changed' in str(response.json)
    response = set_up_client.put('api/v1/admin/8/ntinda/change', content_type='application/json')
    assert response.status_code == 400
    assert 'delivery order 8 you are trying to change does not exist' in json.loads(response.data)['message']
 
 