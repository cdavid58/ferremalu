from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from query_client import Query_Client
from query_inventory import Query_Inventory
from query_invoice import Create_Invoice,Query_Invoice
import json, threading, queue, env, logging, os
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

def Create_Invoice_FE(request):
	request.session['type_invoice'] = 1
	request.session['payment_form'] = 1
	request.session['date_expired'] = str(date.today())
	qc = Query_Client()
	consecutive = qc.GET_CONSECUTIVE(request)
	del qc
	return render(request,'invoice/create_invoice.html',{'type_invoice':'Electrónica','consecutive':consecutive})

def GET_CLIENT(request):
	if request.is_ajax():
		qc = Query_Client()
		query = qc.GET_CLIENT(request.GET['pk'])
		request.session['pk_client'] = request.GET['pk']
		query = json.dumps(query)
		del qc
		return HttpResponse(query)

def GET_PRODUCT(request):
	if request.is_ajax():
		# qi = Query_Inventory()
		# query = qi.GET_PRODUCT(request)
		# del qi
		with open(env.FILE_JSON_INVENTORY) as file:
			data = json.load(file)
		query = None
		print(request.GET['value'])
		for i in range(len(data)):
			if int(data[i]['pk']) == int(request.GET['value']):
				query = data[i]
				break
		print(query)
		return HttpResponse(json.dumps(query))

def Set_Payment_Form(request):
	if request.is_ajax():
		request.session['payment_form'] = int(request.GET['pk'])
		print(request.session['payment_form'])
		return HttpResponse(True)

def Date_Expired(request):
	if request.is_ajax():
		date = request.GET['date_expired'].split('/')
		request.session['date_expired'] = str(date[2])+'-'+str(date[0])+'-'+str(date[1])
		date_ = request.session['date_expired']
		__date = date_.split('-')
		dates = list(map(int, __date))
		days = Count_Days(dates)
		request.session['days_expired'] = days
		return HttpResponse(True)

def Save_Invoice(request):
	if request.is_ajax():
		data = request.GET
		_data = None
		for i in data:
			_data = json.loads(i)
		_data[0]['type'] = request.session['type_invoice']
		payment_form = request.session['payment_form']
		_data[0]['payment_form'] = payment_form
		if payment_form == 1:
			_data[0]['cancelled'] = True
		elif payment_form == 3:
			_data[0]['cancelled'] = True
		elif payment_form == 4:
			_data[0]['cancelled'] = True
		else:
			_data[0]['cancelled'] = False
			_data[0]['days_expired'] = request.session['days_expired']

		_data[0]['employee'] = request.session['employee_pk']
		_data[0]['client'] = request.session['pk_client']
		_data[0]['company'] = request.session['company_pk']
		_data[0]['date'] = str(date.today())
		_data[0]['date_expired'] = request.session['date_expired']
		_data[0]['time'] = "21:45"
		_data[0]['efectivo'] = request.session['efectivo']
		_data[0]['transferencia'] = request.session['trans']

		c = Create_Invoice(request,_data)
		c.Send_Invoice()
	return HttpResponse(True)

def GET_LIST_INVOICE(request):
	from query_invoice import Query_Invoice
	query = Query_Invoice()
	try:
		list_invoice_fe = query.GET_LIST_INVOICE(request,1)
		with open(env.FILE_JSON_INVOICE_FE, 'w') as file:
			json.dump(list_invoice_fe, file, indent=4)
	except Exception as e:
		pass

	return render(request,'list_invoice/invoice.html',{'json':enviroments_json + "/static/data_fe.json"})

def View_Invoice(request,pk):
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

	return render(request,'list_invoice/view_invoice.html',{'details_product':details_product,'total':Thousands_Separator(round(total,2)),
		'subtotal_invoice':Thousands_Separator(round(subtotal_invoice,2)),'tax_invoice':Thousands_Separator(round(tax_invoice,2)), 'iva19':VALUES_TAXES(19,details_product),
		'iva5':VALUES_TAXES(5,details_product), 'iva0':VALUES_TAXES(0,details_product), 'client':client, 'information':informations, 'days_expired':days,'type_invoice':type_invoice})

def VALUES_TAXES(tax,data):
	total_base = 0
	total_tax = 0
	for i in data:
		if tax == i['tax']:
			total_base += i['price_base']
			total_tax = i['val_tax']
	return {str(tax):total_tax,'base':total_base}


def Send_DIAN(request):
	if request.is_ajax:
		consecutive = request.GET['consecutive']
		u = threading.Thread(target=Send_Invoice,args=(request,consecutive,), name='Invoice')
		u.start()
		data = my_queue.get()
		return HttpResponse(data)

@storeInQueue
def Send_Invoice(request,consecutive):
	ci = Create_Invoice(request,'')
	return ci.Send_Invoice_Dian(consecutive)


def Get_PDF_Platform(request,consecutive):
	if validated(request):
		prefix = "FFET"
		try:
			return FileResponse(open(env.URL_PDF_PLATFORM+str(request.session['company_pk'])+'/FES-'+str(prefix)+str(consecutive)+'.pdf','rb'),content_type='application/pdf')
		except Exception as e:
			return FileResponse(open(env.URL_PDF_PLATFORM+str(request.session['company_pk'])+'/FES-'+str(prefix)+str(consecutive)+'.pdf','rb'),content_type='application/pdf')
	return redirect('/error403')



def CreditNote(request,consecutive,type_invoice):
	query = Query_Invoice()
	query.CREDITNOTE(consecutive,type_invoice)
	return HttpResponse('')

def GET_LIST_NOTE_CREDIT(request,type_invoice):
	return render(request,'list_invoice/list_creditnote.html',{'creditnote':Query_Invoice().GetListCreditNote(type_invoice)})


def SetPayment(request):
	if request.is_ajax():
		data = request.GET
		request.session['efectivo'] = data['efectivo']
		request.session['trans'] = data['trans']
		print(request.session['efectivo'])
		print(request.session['trans'])
		return HttpResponse()