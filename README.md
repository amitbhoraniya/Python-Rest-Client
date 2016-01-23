# Python-Rest-Client
Simple Python file it can be useful in every python project for HTTP Requests.

#How to use?
Simple Import http_client.py file in your class.

import http_client as request

##Seng GET Request Without any params
url = 'http://rangoli.finalhints.com'
request.get(url+'/category')

##Seng GET Request With Query Parameters
print request.get(url+'/category',params={'q':'Amit Bhoraniya'})

##Seng GET Request With Custom Header
print request.get(url+'/category',params={'q':'Amit Bhoraniya'},header={'content-type':'application/json'})
