from django.http import HttpResponse
from django.shortcuts import render,redirect
from .query_api import Query_API
import json, requests, env,time
from from_number_to_letters import Thousands_Separator

enviroments_json = env.ENVIROMENT_JSON

def Login(request):
	if request.is_ajax():
		data = request.GET
		q = Query_API()
		result = q.validate_login(data,request)
		del q
		return HttpResponse(result)
	return render(request,'login.html')

def Add_Employee(request):
	if request.is_ajax():
		data = request.data
		return HttpResponse(True)
	return render(request,'inventory/add.html')

def Close_Box(request):
	url = env.CLOSE_BOX_TOTAL
	payload = json.dumps({})
	headers = {
	  'Content-Type': 'application/json'
	}
	response = requests.request("POST", url, headers=headers, data=payload)



def LogOut(request):
	start = request.session['work_start']
	print(time.time() - start)
	for i,j in list(request.session.items()):
		del request.session[i]
	Close_Box(request)
	return redirect('/')

def Refresh_Employee(request):
	url = env.GET_LIST_EMPLOYEE
	payload = json.dumps({"company": request.session['company_pk']})
	headers = {'Content-Type': 'application/json'}
	response = requests.request("POST", url, headers=headers, data=payload)
	with open(env.LIST_EMPLOYEE,'w') as file:
		json.dump(json.loads(response.text),file,indent=4)
	print(response.text)

def GET_LIST_EMPLOYEE(request):
	Refresh_Employee(request)
	return render(request,'employee/list_employee.html',{'json':enviroments_json + "/static/employee.json"})

def Edit(request,pk):
	url = env.GET_EMPLOYEE
	payload = json.dumps({"pk_employee": pk})
	headers = {'Content-Type': 'application/json'}
	response = requests.request("POST", url, headers=headers, data=payload)
	employee = json.loads(response.text)
	request.session['employee_updated'] = pk
	return render(request,'employee/edit.html',{'e':employee})

def UPDATED_EMPLOYEE(request):
	if request.is_ajax():
		data = request.GET
		_data = {
			"pk": request.session['employee_updated'],
			"documentI": data['documentI'],
			"name": data['name'],
			"phone": data['phone'],
			"email": data['email'],
			"user": data['user'],
			"psswd": data['psswd'],
			"type_employee": data['type_employee']
		}
		result = Query_API().EDIT_EMPLOYEE(_data)
		url = env.GET_LIST_EMPLOYEE
		payload = json.dumps({"company": request.session['company_pk']})
		headers = {'Content-Type': 'application/json'}
		response = requests.request("POST", url, headers=headers, data=payload)
		with open(env.LIST_EMPLOYEE,'w') as file:
			json.dump(json.loads(response.text),file,indent=4)
		return HttpResponse(result)


def CREATE_EMPLOYEE(request):
	if request.is_ajax():
		return HttpResponse(json.dumps(Query_API().CREATE_EMPLOYEE(request)))
	return render(request,'employee/add.html')

def DELETE_EMPLOYEE(request):
	if request.is_ajax():
		message = Query_API().DELETE_EMPLOYEE(request.GET['pk'])
		Refresh_Employee(request)
		return HttpResponse(message)

def Get_List_Close_Box(request):
	url = env.GET_LIST_CLOSE_BOX
	payload = json.dumps({})
	headers = {'Content-Type': 'application/json'}
	response = requests.request("POST", url, headers=headers, data=payload)
	response_dict = json.loads(response.text)
	total = 0
	for i in response_dict:
		total += (float(i['efec']) + float(i['cred']) + float(i['trans']))
	return render(request,'report/close_box.html',{'close_box':response_dict,'total':Thousands_Separator(round(total,0))})





















