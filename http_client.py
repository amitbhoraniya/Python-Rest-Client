import urllib2 as http
import urllib
import json

def post(url,*positional_params,**keyword_parameters):
	
	if('url_param' in keyword_parameters):
		req = http.Request(url+"?"+urllib.urlencode(keyword_parameters['url_param']))
	else:
		req = http.Request(url)
	
	if('params' in keyword_parameters):
		req.add_data(json.dumps(keyword_parameters['params']))

	
	if('header' in keyword_parameters):
		for key,value in (keyword_parameters['header']).iteritems():
			req.add_header(key,value)

	r = http.urlopen(req)
	return r.read()

def get(url,*positional_params,**keyword_parameters):
	
	if('params' in keyword_parameters):
		req = http.Request(url+"?"+urllib.urlencode(keyword_parameters['params']))
	else:
		req = http.Request(url)

	if('header' in keyword_parameters):
		for key,value in (keyword_parameters['header']).iteritems():
			req.add_header(key,value)

	r = http.urlopen(req)
	return r.read()