"""temporary data store"""

PARCELS = []

def add_parcel(pick_up, drop_off, parcel_name, description, user_id):
    """create a parcel delivery order and update the temporary store"""
    parcel = {
        'parcel_id' : len(PARCELS) + 1,
        'pick_up': pick_up,
        'drop_off':drop_off,
        'parcel_name':parcel_name,
        'description':description,
        'user_id':user_id,
        'status':'transit',
        'location':'currently moving'
        }
    PARCELS.append(parcel)
    return PARCELS
        