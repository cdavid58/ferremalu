from django.conf.urls import url
from .views import *

urlpatterns=[
		url(r'^Create_Invoice_POS/$',Create_Invoice_POS,name="Create_Invoice_POS"),
		url(r'^GET_LIST_INVOICE_POS/$',GET_LIST_INVOICE_POS,name="GET_LIST_INVOICE_POS"),
		url(r'^Type_Sell/$',Type_Sell,name="Type_Sell"),
		url(r'^Invoice_Print/(\d+)/$',Invoice_Print,name="Invoice_Print"),
		url(r'^DiscountStock/$',DiscountStock,name="DiscountStock"),
		url(r'^IncrementStock/$',IncrementStock,name="IncrementStock"),
		url(r'^Date_Expired_POS/$',Date_Expired_POS,name="Date_Expired_POS"),
		url(r'^UPDATE_WALLET_POS/$',UPDATE_WALLET_POS,name="UPDATE_WALLET_POS"),
	]