"""CONTAINS API ENDPOINTS"""
from flask import jsonify, request
from app.apiv1 import bp
from .modals import Parcels
from .errors import bad_request

@bp.route('/parcels', methods=['POST'])
def make_a_delivery_order():
    """Create a parcel delivery order"""
    order = request.get_json() or {}

    #check for an empty post
    if not order:
        return bad_request("You entered nothing")

    #check for empty values in post and return missing field
    for key, value in order.items():
        if value == "":
            return bad_request("You are missing {} in your input".format(key))

    #check for missing keys
    for key in order:
        if len(order) < 6:
            return bad_request("You are missing a required field")

    #create parcel with received input
    one_order = Parcels()
    one_order.add_parcel(order['pick_up'], order['recepient'], order['drop_off'],
                         order['parcel_name'], order['description'], order['weight'])
    return jsonify("Delivery order created"), 201
