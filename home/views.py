from query_invoice import Query_Invoice
from django.shortcuts import render
import json, env, threading, queue, requests, time, logging, os
from query_client import Query_Client
from query_inventory import Query_Inventory

my_queue = queue.Queue()
enviroments = env.ENVIROMENT
def storeInQueue(f):
  def wrapper(*args):
  	global my_queue
  	my_queue.put(f(*args))
  return wrapper

def Index(request):
	if 'work_start' not in request.session:
		request.session['work_start'] = time.time()
# 		Generated_File(request)<<
	return render(request,'index.html')

@storeInQueue
def Generated_File(request):
	try:
		query = Query_Invoice()
		list_invoice_fe = query.GET_LIST_INVOICE(request,1)
		with open(env.FILE_JSON_INVOICE_FE, 'w') as file:
			json.dump(list_invoice_fe, file, indent=4)

		list_invoice_pos = query.GET_LIST_INVOICE(request,2)
		with open(env.FILE_JSON_INVOICE_POS, 'w') as file:
			json.dump(list_invoice_pos, file, indent=4)

		list_client = Query_Client().GET_LIST_CLIENT(request)
		with open(env.FILE_JSON_CLIENTS, 'w') as file:
			json.dump(list_client, file, indent=4)

		list_inventory = Query_Inventory().GET_LIST_INVENTORY(request)
		with open(env.FILE_JSON_INVENTORY, 'w') as file:
			json.dump(list_inventory, file, indent=4)

		url = env.GET_LIST_EMPLOYEE
		payload = json.dumps({"company": request.session['company_pk']})
		headers = {'Content-Type': 'application/json'}
		response = requests.request("POST", url, headers=headers, data=payload)
		with open(env.LIST_EMPLOYEE,'w') as file:
			json.dump(json.loads(response.text),file,indent=4)

		del query
	except Exception as e:
		pass