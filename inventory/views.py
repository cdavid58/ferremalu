from django.http import HttpResponse
from django.shortcuts import render
import json,env, threading, queue, requests, urllib, logging, os
from query_inventory import Query_Inventory

enviroments_json = env.ENVIROMENT_JSON

def List_Inventory(request):
	list_inventory = Query_Inventory().GET_LIST_INVENTORY(request)
	with open(env.FILE_JSON_INVENTORY, 'w') as file:
		json.dump(list_inventory, file, indent=4)
	return render(request,'inventory/list_inventory.html',{'json':enviroments_json+"/static/inventory.json"})

def Add_Product(request):
	return render(request,'inventory/add.html')

def Edit_Product(request,pk):
	with open(env.FILE_JSON_INVENTORY) as file:
		data = json.load(file)
	product = None
	request.session['pk_product'] = pk
	for i in data:
		if str(pk) == str(i['pk']):
			product = i
			break
	return render(request,'inventory/edit.html',{'p':product})

def UPDATED_PRODUCT(request):
	if request.is_ajax():
		data = request.GET
		_data = {
	    "pk":request.session['pk_product'],
	    "name":data['name'],
	    "tax":data['tax'],
	    "quanty":data['quanty'],
	    "cost":data['cost'],
	    "price_1":data['price_1'],
	    "price_2":data['price_2'],
	    "price_3":data['price_3'],
	    "price_4":data['price_4'],
	    "price_5":data['price_5'],
	    "company":request.session['company_pk']
		}
		del request.session['pk_product']
		result = Query_Inventory().UPDATED_PRODUCT(_data)
		message = result['message']
		if result['result']:
			message = result['message']
			Refresh_List_Inventory(request)
		return HttpResponse(result['result'])		

my_queue = queue.Queue()
def storeInQueue(f):
  def wrapper(*args):
  	global my_queue
  	my_queue.put(f(*args))
  return wrapper

def Refresh_List_Inventory(request):
	path = env.ENVIROMENT_FOLDER_LOG + 'refresh_list_inventory.log'
	if os.path.exists(path):
		os.remove(path)
	logging.basicConfig(filename=path, encoding='utf-8', level=logging.DEBUG)
	try:
		list_inventory = Query_Inventory().GET_LIST_INVENTORY(request)
		with open(env.FILE_JSON_INVENTORY, 'w') as file:
			json.dump(list_inventory, file, indent=4)
	except Exception as e:
		logging.error(str(e))
	

def Save_Product(request):
	if request.is_ajax():
		data = request.GET
		result = Query_Inventory().CREATE_PRODUCT(request,data)
		Refresh_List_Inventory(request)
		return HttpResponse(result)

def DELETE_PRODUCT(request):
	if request.is_ajax():
		data = request.GET
		_data = {
			'company':request.session['company_pk'],
			'code':data['code']
		}
		result = Query_Inventory().DELETE_PRODUCT(_data)
		Refresh_List_Inventory(request)
		return HttpResponse(result)

from plyer import notification

def Montage_Inventory(request):
	if request.is_ajax():
		data = request.POST
		data_inventory = []
		for j in json.loads(data['data_inventory']):
			data_inventory.append(
				{
					"code": j['CODIGO'],
				  "name": j['PRODUCTO'],
				  "quanty": j['CANTIDAD'],
				  "tax": j['IVA'],
				  "cost": j['COSTO'],
				  "price_1": j['PRECIO1'],
				  "price_2": j['PRECIO2'],
				  "price_3": j['PRECIO3'],
				  "price_4": j['PRECIO4'],
				  "price_5": j['PRECIO5']
				}
			)

		u = threading.Thread(target=Montage,args=(request,data_inventory,), name='Invoice')
		u.start()
		result = my_queue.get()
		if result:
			notification.notify(
				title='EXITO',
				app_name="Evansoft",
				message='Proceso finalizado',
				app_icon = "./static/favicon.ico"
			)
		return HttpResponse(data)
	return render(request,'inventory/montage_inventory.html')

@storeInQueue
def Montage(request,data):
	result = Query_Inventory().CREATE_PRODUCT_EXCEL(request,data)
	return result
