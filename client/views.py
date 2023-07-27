from django.http import HttpResponse
from django.shortcuts import render
from query_client import Query_Client
import requests, json, env, threading, queue, logging, os

my_queue = queue.Queue()
enviroments_json = env.ENVIROMENT_JSON

def storeInQueue(f):
  def wrapper(*args):
  	global my_queue
  	my_queue.put(f(*args))
  return wrapper

def List_Client(request):
	GET_CLIENT_LIST(request)
	return render(request,'client/list_client.html',{'json':enviroments_json + "/static/clients.json"})

def GET_CLIENT_LIST(request):
	try:
		list_client = Query_Client().GET_LIST_CLIENT(request)
		with open(env.FILE_JSON_CLIENTS, 'w') as file:
			json.dump(list_client, file, indent=4)
		del list_client
	except Exception as e:
		pass


def Add_Client(request):
	return render(request,'client/add.html')

def CREATE_CLIENT(request):
	if request.is_ajax():
		data = request.GET
		query = Query_Client().CREATE_CLIENT(request,data)
		GET_CLIENT_LIST(request)
	return HttpResponse(json.dumps(query))

def DELETE_CLIENT(request):
	if request.is_ajax():
		result = Query_Client().DELETE_CLIENT(request.GET)
		if result:
			GET_CLIENT_LIST(request)
		return HttpResponse(result)

def Edit_Client(request,pk):
	qc = Query_Client().GET_CLIENT(pk)
	request.session['pk_client'] = pk
	return render(request,'client/edit.html',{'c':qc})

def EDIT_CLIENT(request):
	if request.is_ajax():
		data = request.GET
		identification_number = data['identification_number'].split('-')
		_data = {
			"pk":request.session['pk_client'],
	    "identification_number":identification_number[0],
	    "dv":identification_number[1],
	    "name":data['name'],
	    "phone":data['phone'],
	    "address":data['address'],
	    "email":data['email'],
	    "merchant_registration":None,
	    "type_documentI":data['type_documentI'],
	    "type_organization":data['type_organization'],
	    "type_regime":data['type_regime'],
	    "municipality":data['municipality'],
	    "type_client":data['type_client']
		}
		print(_data)
		qc = Query_Client().EDIT_CLIENT(_data)
		if qc['result']:
			GET_CLIENT_LIST(request)
		return HttpResponse(qc['result'])



