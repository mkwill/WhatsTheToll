import requests
from app import app

@app.route("/", methods = ['Get','Post'])
def user_handler():
    url = 'https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyDsPuOzu2Twbyvd5ajeimu35hsDzXAoUcA'
    req = requests.post(url)
    req
    data = req.json()
    print(data)
    return data