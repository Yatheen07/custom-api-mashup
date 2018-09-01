# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 21:32:06 2018

@author: kmy07
"""

import json, requests
url = 'https://api.foursquare.com/v2/venues/explore'

def getParams(foodItem,long,lat):
    params = dict(
      client_id='LWEFMZENDEDBGTZM5A1A3U4OAS1EOCF3OTICMO3K0WB23IJF',
      client_secret='1H43KIVZGKV50NG5PYODLMSBPWD1W2TNQIDSTTKJFGSTZFZ5',
      v='20180323',
      ll='28.6139391,77.2090212',
      query=str(foodItem),
      limit=1
      )
    
    return params

parameters = getParams('coffee',13.0367914,80.2676303)
resp = requests.get(url=url, params=parameters)
data = json.loads(resp.text)
print(data)