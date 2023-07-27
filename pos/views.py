from django.shortcuts import render
from django.http import HttpResponse
from query_client import Query_Client
from query_inventory import Query_Inventory
from query_invoice import Create_Invoice,Query_Invoice
import json, threading, queue, env, requests
from date import Count_Days
from datetime import date
from from_number_to_letters import Thousands_Separator

my_queue = queue.Queue()
enviroments_json = env.ENVIROMENT_JSON

def storeInQueue(f):
  def wrapper(*args):
  	global my_queue
  	my_queue.put(f(*args))
  return wrapper


def GetAmount(request):
	url = "https://apiferre.pythonanywhere.com/close_box/Get_Total_Sell/"
	payload = json.dumps({})
	headers = {
	  'Content-Type': 'application/json'
	}
	response = requests.request("POST", url, headers=headers, data=payload)
	return json.loads(response.text)['totals']

def Date_Expired_POS(request):
	if request.is_ajax():
		date = request.GET['date_expired'].split('-')[1].strip()
		request.session['date_expired'] = date
		return HttpResponse(True)

@storeInQueue
def GetInventory(request):
	list_inventory = Query_Inventory().GET_LIST_INVENTORY(request)
	with open(env.FILE_JSON_INVENTORY, 'w') as file:
		json.dump(list_inventory, file, indent=4)


def Create_Invoice_POS(request):
	request.session['type_invoice'] = 2
	qc = Query_Client()
	query = qc.GET_LIST_CLIENT(request)
	consecutive = qc.GET_CONSECUTIVE(request)
	qi = Query_Inventory()
	inventory_query = qi.GET_LIST_INVENTORY(request)
	request.session['consecutive'] = consecutive
	request.session['type_sell'] = 1
	request.session['pk_client'] = 31
	request.session['days_expired'] = 0
	del qc
	request.session['payment_form'] = 1
	request.session['date_expired'] = str(date.today())
	request.session['efectivo'] = 0
	request.session['trans'] = 0
	return render(request,'invoice/create_invoice.html',{'client':query,'type_invoice':'POS','query':query,'consecutive':consecutive,'inventory':inventory_query})

def GET_LIST_INVOICE_POS(request):
	request.session['type_invoice'] = 2
	query = Query_Invoice()
	list_invoice_pos = query.GET_LIST_INVOICE(request,2)
	with open(env.FILE_JSON_INVOICE_POS, 'w') as file:
		json.dump(list_invoice_pos, file, indent=4)
	return render(request,'list_invoice/invoice.html',{'json':enviroments_json + '/static/data_pos.json'})

def Type_Sell(request):
	if request.is_ajax():
		request.session['type_sell'] = request.GET['type_sell']
		print(request.session['type_sell'])
	return HttpResponse(request.GET['type_sell'])

def DiscountStock(request):
	if request.is_ajax():
		inf = request.GET
		with open(env.FILE_JSON_INVENTORY) as file:
			data = json.load(file)
		for i in range(len(data)):
			if data[i]['code'] == inf['code']:
				type_sell = inf['type_sell']
				print(type_sell)
				if type_sell == 'Completo':
					data[i]['quanty'] = int(data[i]['quanty']) - int(inf['quanty'])
				elif type_sell == 'Metros':
					data[i]['metro'] = int(data[i]['metro']) - int(inf['quanty'])
				elif type_sell == "Unidad":
					data[i]['und'] = int(data[i]['und']) - int(inf['quanty'])
				with open(env.FILE_JSON_INVENTORY, 'w') as file:
					json.dump([], file, indent=4)
				with open(env.FILE_JSON_INVENTORY, 'w') as file:
					json.dump(data, file, indent=4)
				break

		return HttpResponse('less')


def IncrementStock(request):
	if request.is_ajax():
		inf = request.GET
		print(inf)
		with open(env.FILE_JSON_INVENTORY) as file:
			data = json.load(file)
		for i in range(len(data)):
			if data[i]['code'] == inf['code']:
				type_sell = inf['type_sell']
				print(type_sell)
				if type_sell == 'Completo':
					data[i]['quanty'] = int(data[i]['quanty']) + int(inf['quanty'])
				elif type_sell == 'Metros':
					data[i]['metro'] = int(data[i]['metro']) + int(inf['quanty'])
				elif type_sell == "Unidad":
					data[i]['und'] = int(data[i]['und']) + int(inf['quanty'])
				with open(env.FILE_JSON_INVENTORY, 'w') as file:
					json.dump([], file, indent=4)
				with open(env.FILE_JSON_INVENTORY, 'w') as file:
					json.dump(data, file, indent=4)
				break

		return HttpResponse('add')





def Invoice_Print(request,pk):
	query = Query_Invoice()
	data = query.GET_INVOICE(pk,request)
	details_product = data['product']
	informations = data['information']
	client = data['client']
	subtotal_invoice = 0
	tax_invoice = 0
	for i in details_product:
		subtotal_invoice += i['subtotal']
		tax_invoice += i['val_tax']
	total = subtotal_invoice + tax_invoice
	del query
	date_ = str(informations['date_expired'])
	_date = date_.split('-')
	dates = list(map(int, _date))
	days = Count_Days(dates)
	if informations['payment_form'] == "Contado":
		days = 0
	type_invoice = "Electrónica"
	if request.session['type_invoice'] == 2:
		type_invoice = "POS"

	return render(request,'invoice_ticket.html',{'details_product':details_product,'total':Thousands_Separator(round(total,2)),
		'subtotal_invoice':Thousands_Separator(round(subtotal_invoice,2)),'tax_invoice':Thousands_Separator(round(tax_invoice,2)),'client':client, 'information':informations, 'days_expired':days,'type_invoice':type_invoice})


def UPDATE_WALLET_POS(request):
	if request.is_ajax():
		data = request.GET
		Query_Invoice().UPDATE_WALLET(data['pk'],data['payment_form'],request.session['employee_pk'])
		return HttpResponse('')































