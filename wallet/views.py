from django.http import HttpResponse
from django.shortcuts import render
import json,requests,env

def Get_Wallet_POS(request):
	url = env.GET_INVOICE_CREDIT
	payload = json.dumps({})
	headers = {
	  'Content-Type': 'application/json'
	}
	response = requests.request("POST", url, headers=headers, data=payload)
	response_dict = json.loads(response.text)
	total = 0
	for i in response_dict:
		total += float(i['total'])
	return render(request,'wallet/credit_pos_invoice.html',{'data':response_dict,'total':total})

def Cancelled(request):
	if request.is_ajax():
		data = request.GET
		print(data)
		return HttpResponse(True)