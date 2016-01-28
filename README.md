# Python-Rest-Client
Simple Python file it can be useful in every python project for HTTP Requests.

##How to use?
Simple Import http_client.py file in your class.
```python
import http_client as request
```
###Send GET Request Without any params
```python
url = 'http://rangoli.finalhints.com'
request.get(url+'/category')
```

###Send GET Request With Query Parameters
```python
request.get(url+'/category',params={'search':'Amit Bhoraniya'})
```
###Send GET Request With Custom Header
```python
request.get(url+'/category',params={'search':'Amit Bhoraniya'},header={'content-type':'application/json'})
```
