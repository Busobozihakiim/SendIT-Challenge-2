"""MAKING CUSTOM ERROR"""
from flask import jsonify
from werkzeug.http import HTTP_STATUS_CODES

def error_response(status_code, message=None):
    """
    Gets short desciptive name from the HTTP_STATUS_CODES
    dictionary puts it in the payload dictionary and appends
    a messages you defined and returns the new user friendly error
    """
    payload = {'error': HTTP_STATUS_CODES.get(status_code, 'Unknown error')}
    if message:
        payload['message'] = message
    response = jsonify(payload)
    response.status_code = status_code
    return response

def bad_request(message):
    """this will handle the 400 bad request"""
    return error_response(400, message)
