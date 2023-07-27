import json, requests, env

class Query_API:
	def validate_login(self,data,request):
		url = env.VALIDATE_LOGIN
		payload = json.dumps({
		  "user": data['user'],
		  "psswd": data['psswd']
		})
		headers = {
		  'Content-Type': 'application/json'
		}
		response = requests.request("POST", url, headers=headers, data=payload)
		result = json.loads(response.text)
		if result['result']:
			request.session['name_user'] = data['user']
			request.session['employee_pk'] = result['employee']
			request.session['company_pk'] = result['company']
			request.session['prefix'] = result['prefix']
			request.session['nit_company'] = result['nit_company']
			request.session['type_employee'] = int(result['type_employee'])
		return result['result']

	def EDIT_EMPLOYEE(self,data):
		url = env.EDIT_EMPLOYEE
		payload = json.dumps(data)
		headers = {'Content-Type': 'application/json'}
		response = requests.request("POST", url, headers=headers, data=payload)
		return json.loads(response.text)['result']


	def CREATE_EMPLOYEE(self,request):
		url = env.REGISTER_EMPLOYEE
		data = request.GET
		payload = json.dumps({
		  "documentI": request.GET['docI'],
		  "name": request.GET['name'],
		  "phone": request.GET['phone'],
		  "email": request.GET['email'],
		  "user": request.GET['user'],
		  "psswd": request.GET['psswd'],
		  "type_employee": request.GET['type_employee'],
		  "company": request.session['company_pk']
		})
		headers = {'Content-Type': 'application/json'}
		response = requests.request("POST", url, headers=headers, data=payload)
		return json.loads(response.text)

	def DELETE_EMPLOYEE(self,pk):
		url = "https://apiferre.pythonanywhere.com/employee/DELETE_EMPLOYEE/"
		payload = json.dumps({"pk": pk})
		headers = {'Content-Type': 'application/json'}
		response = requests.request("POST", url, headers=headers, data=payload)
		return json.loads(response.text)['message']


