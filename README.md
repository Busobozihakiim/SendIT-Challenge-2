# SendIT-Challenge-2
SendIT courier app api

## Features
- `Create a parcel delivery order` User should be able to create a parcel delivery order
- `Get all parcel delivery orders` User should be able to fetch all delivery orders
- `Get a specific parcel delivery order` User should be able to fetch a delivery order by its id
- `Cancel a parcel delivery order` User should be able to cancel a delivery order by its id 
- `Get all parcel delivers by userid` User should be able to fetch all delivery orders by a userid

## Installing
First clone this repository

```
git clone https://github.com/Busobozihakiim/SendIT-Challenge-2/tree/develop
cd SendIT-Challenge-2

Then create a virtual environment and start it
```
virtualenv venv
source/venv/bin/activate
```

Then install all the necessary dependencies
```
pip install -r requirements.txt
```

## Running
At the terminal type in
```
python run.py
```

To run tests run this command at the console/terminal
```
pytest
```
## API Endpoints
|  EndPoint  |  Functionality  |
| ------------- | ------------- |
| GET /parcels  | Fetch all parcel delivery orders  |
| GET /parcels/\<parcel_id\>  | Fetch a specific parcel delivery order  |
| GET /users/\<user_id\>/parcels | Fetch all parcel delivery orders by a specific user |
| PUT /parcels/\<parcel_id\>/cancel | Cancel the specific parcel delivery order |
| POST /parcels | Create a parcel delivery order |
  
## Contributers
- Busobozihakiim

