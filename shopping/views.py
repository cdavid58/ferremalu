from django.http import HttpResponse
from django.shortcuts import render
from datetime import date
import env, json
from query_shopping import QUERY_SHOPPING
from query_inventory import Query_Inventory

def Create_Shopping(request):
	today = date.today()
	list_inventory = Query_Inventory().GET_LIST_INVENTORY(request)
	with open(env.FILE_JSON_INVENTORY, 'w') as file:
		json.dump(list_inventory, file, indent=4)
	months = ("Enero", "Febrero", "Marzo", "Abri", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
	return render(request,'shopping/add.html',{'today':str(today.day)+' '+str(months[today.month - 1])+' '+str(today.year)})

def QUERY_SHOPPINGS(request):
	if request.is_ajax():
		return HttpResponse(QUERY_SHOPPING().CHECK_INVOICE_NUMBER(request))

def Get_Product(request):
	if request.is_ajax():
		with open(env.FILE_JSON_INVENTORY) as file:
			data = json.load(file)
		_data = {}
		for i in data:
			if str(i['code']) == str(request.GET['code']):
				_data = i
	return HttpResponse(json.dumps(_data))

def Save_Shopping(request):
	if request.is_ajax():
		result = QUERY_SHOPPING().SAVE_SHOPPING(request)['result']
		list_inventory = Query_Inventory().GET_LIST_INVENTORY(request)
		with open(env.FILE_JSON_INVENTORY, 'w') as file:
			json.dump(list_inventory, file, indent=4)
		return HttpResponse(result)



def Test(request):
	return render(request,'bars_code.html')

