"""CONTAINS API ENDPOINTS"""
from flask import jsonify, request
from app.apiv1 import bp
from .modals import add_parcel, PARCELS
from .errors import bad_request

@bp.route('/parcels', methods=['POST'])
def make_a_delivery_order():
    """Create a parcel delivery order"""
    order = request.get_json() or {}
    #check for an empty post and missing keys
    if not order:
        return bad_request("You entered nothing")
    for key in order:
        if len(order) < 5:
            return bad_request("You are missing a required field")

    #check for empty values in post and return missing field
    for key, value in order.items():
        if value == "":
            return bad_request("You are missing {} in your input".format(key))

    #create a delivery order
    add_parcel(order['pick_up'], order['drop_off'], order['parcel_name'],
               order['description'], order['user_id'])
    return jsonify("Delivery order created"), 201

@bp.route('/parcels', methods=['GET'])
def see_all_orders():
    """To see all available delivery orders"""
    if PARCELS:
        return jsonify("Available Delivery Orders", PARCELS), 200
    return jsonify("You dont have any delivery orders"), 200

@bp.route('/parcels/<int:parcel_id>', methods=['GET'])
def get_order_by_id(parcel_id):
    """To see an available delivery order by its id"""
    try:
        if PARCELS:
            order = [this_id for this_id in PARCELS if this_id['parcel_id'] == parcel_id]
            return jsonify("Here is the delivery order of id {}".format(parcel_id), order[0]), 200
        return jsonify("No deliveries made yet"), 200
    except IndexError:
        return jsonify("this delivery order of id {} doesnt exist".format(parcel_id)), 200

@bp.route('/users/<string:userid>/parcels', methods=['GET'])
def get_all_orders_by_userid(userid):
    """Fetch all delivery orders by user_id"""
    if not PARCELS:
        return jsonify("You have not made any delivery orders"), 200
    user = [user for user in PARCELS if user['user_id'] == userid]
    if len(user) != 0:
        return jsonify("here is the delivery order of {}".format(userid), user), 200
    return jsonify("The user {} doesnt have parcels and doesnt exist".format(userid))

@bp.route('/parcels/<int:parcel_id>/cancel', methods=['PUT'])
def cancel_delivery_order(parcel_id):
    """Cancel a parcel delivery order"""
    try:
        if PARCELS:
            cancel = [this_order for this_order in PARCELS if this_order['parcel_id'] == parcel_id]
            cancel[0]['status'] = 'Cancel'
            return jsonify('delivery order has been canceled'), 200
        return jsonify('You have no delivery orders')
    except IndexError:
        return jsonify('Delivery order {} not found'.format(parcel_id)), 200

@bp.route('/admin/<int:parcel_id>/<string:location>/change', methods=['PUT'])
def change_location(parcel_id, location):
    """changes the current location
    Given the user id and the new location"""
    try:
        if PARCELS:
            locale = [current for current in PARCELS if current['parcel_id'] == parcel_id]
            locale[0]['location'] = '{}'.format(location)
            return jsonify('current location has been changed')
        return jsonify('You have no delivery orders')
    except IndexError:
        return bad_request('delivery order {} you are trying to change does not exist'.format(parcel_id))
 