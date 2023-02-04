from django.conf.urls import url
from .views import *

urlpatterns=[
		url(r'^Create_Invoice_POS/$',Create_Invoice_POS,name="Create_Invoice_POS"),
		url(r'^GET_LIST_INVOICE_POS/$',GET_LIST_INVOICE_POS,name="GET_LIST_INVOICE_POS"),
	]