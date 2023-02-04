import json,requests,env
from date import date

class QUERY_SHOPPING:
	def CHECK_INVOICE_NUMBER(self,request):
		url = env.CHECK_INVOICE_NUMBER
		payload = json.dumps({
		  "invoice_number": request.GET['invoice_number'],
		  "company": request.session['company_pk']
		})
		headers = {'Content-Type': 'application/json'}
		response = requests.request("POST", url, headers=headers, data=payload)
		result = json.loads(response.text)['result']
		request.session['invoice_number'] = request.GET['invoice_number']
		return result

	def SAVE_SHOPPING(self,request):
		url = env.CREATE_SHOPPINGS
		data = {}
		data['shopping'] = {
			"invoice_number": int(request.session['invoice_number']),
			"date": "2022-01-14",
			"employee": request.session['employee_pk'],
			"total": 0
		}
		data['shopping_lines'] = [ i for i in request.GET]
		payload = json.dumps(data)
		print(payload)
		headers = {'Content-Type': 'application/json'}
		response = requests.request("POST", url, headers=headers, data=payload)
		return json.loads(response.text)

