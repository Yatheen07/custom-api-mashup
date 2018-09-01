# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 20:53:37 2018

@author: kmy07
"""

import httplib2
import json

def getGoogleApiKey():
    with open("./google_api.txt",'rb') as file:
        google_api = file.read()
    google_api = google_api.decode("utf-8")
    return google_api

def getLocation(inputString):
    google_api_key = getGoogleApiKey()
    locationString = inputString.replace(" ","+")
    url = ('https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s'%(locationString,google_api_key))
    request = httplib2.Http()
    response , content = request.request(url,'GET')
    #print("Response is: "+str(response))
    result = json.loads(content)
    #print(result)
    return result 
    


result = getLocation("New Delhi,India")
lat = result['results'][0]['geometry']['location']['lat']
lng = result['results'][0]['geometry']['location']['lng']

print("Latitude: "+str(lat))
print("Longitude: "+str(lng))