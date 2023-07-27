from django.shortcuts import render
import env, json, requests

enviroments = env.ENVIROMENT

class Query_Client:
	def GET_LIST_CLIENT(self,request):
		url = env.GET_LIST_CLIENT
		payload = json.dumps({
		  "company": request.session['company_pk']
		})
		headers = {
		  'Content-Type': 'application/json'
		}
		response = requests.request("POST", url, headers=headers, data=payload)
		return json.loads(response.text)['client']

	def GET_CLIENT(self,pk):
		url = env.GET_CLIENT
		payload = json.dumps({
		  "pk": pk
		})
		headers = {
		  'Content-Type': 'application/json'
		}
		response = requests.request("POST", url, headers=headers, data=payload)
		client = json.loads(response.text)['client']
		return client

	def GET_CONSECUTIVE(self,request):
		url = env.GET_CONSECUTIVE
		payload = json.dumps({
		  "company":request.session['company_pk'],
		  "type_invoice":request.session['type_invoice']
		})
		headers = {'Content-Type': 'application/json'}
		response = requests.request("POST", url, headers=headers, data=payload)
		return json.loads(response.text)['consecutive']

	def DELETE_CLIENT(self,data):
		url = env.DELETE_CLIENT
		payload = json.dumps({
			'pk':data['pk']
		})
		headers = {'Content-Type': 'application/json'}
		response = requests.request("POST", url, headers=headers, data=payload)
		return json.loads(response.text)['client']

	def CREATE_CLIENT(self,request,data):
		url = env.CREATE_CLIENT
		try:
			doc = str(data['docI']).split('-')
			cc = doc[0]
			dv = doc[1]
		except Exception as e:
			cc = data['docI'][:len(data['docI']) - 1]
			dv = data['docI'][:-1]
		payload = json.dumps({
		  "identification_number": cc,
		  "dv": dv,
		  "name": data['name'],
		  "phone": data['phone'] if data['phone'] != "" else None,
		  "address": data['address'] if data['address'] != "" else None,
		  "email": data['email'] if data['email'] != "" else None,
		  "merchant_registration": None,
		  "type_documentI": data['type_document'],
		  "type_organization": data['organization'],
		  "type_regime": data['regime'],
		  "municipality": data['municipality'],
		  "company": request.session['company_pk']
		})
		headers = {
		  'Content-Type': 'application/json'
		}
		response = requests.request("POST", url, headers=headers, data=payload)
		return json.loads(response.text)#['result']

	def EDIT_CLIENT(self,data):
		url = env.EDIT_CLIENT
		payload = json.dumps(data)
		headers = {'Content-Type': 'application/json'}
		response = requests.request("POST", url, headers=headers, data=payload)
		return json.loads(response.text)['result']


