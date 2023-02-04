from django.shortcuts import render
from query_invoice import Query_Invoice
import env, json

def Invoice(request):
	query = Query_Invoice()
	list_invoice_pos = query.GET_LIST_INVOICE(request,2)
	with open(env.FILE_JSON_INVOICE_POS, 'w') as file:
		json.dump(list_invoice_pos, file, indent=4)
	return render(request,'report/invoice.html',{'json':'http://localhost:8000/static/data_pos.json'})
