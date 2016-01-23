import http_client as request

url = 'http://rangoli.finalhints.com'

#GET Request Example
print request.get(url+'/category',params={'q':'Amit Bhoraniya'},header={'content-type':'application/json'})