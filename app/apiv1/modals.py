"""temporary data store"""

PARCELS = []

class Parcels:
    """class to create parcel delivery order"""

    def __init__(self):
        pass

    def add_parcel(self, pick_up, recepient, drop_off, parcel_name, description, weight, user_id):
        """create a parcel delivery order and update the temporary store"""
        parcel = {
            'parcel_id' : len(PARCELS) + 1,
            'pick_up': pick_up,
            'recepient':recepient,
            'drop_off':drop_off,
            'parcel_name':parcel_name,
            'description':description,
            'weight':weight,
            'user_id':user_id,
            'status':'transit'
        }
        PARCELS.append(parcel)
        return PARCELS
        