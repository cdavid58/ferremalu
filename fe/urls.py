from django.conf.urls import url
from .views import *

urlpatterns=[
		url(r'^Create_Invoice_FE/$',Create_Invoice_FE,name="Create_Invoice_FE"),
		url(r'^GET_CLIENT/$',GET_CLIENT,name="GET_CLIENT"),
		url(r'^GET_PRODUCT/$',GET_PRODUCT,name="GET_PRODUCT"),
		url(r'^Save_Invoice/$',Save_Invoice,name="Save_Invoice"),
		url(r'^Set_Payment_Form/$',Set_Payment_Form,name="Set_Payment_Form"),
		url(r'^Date_Expired/$',Date_Expired,name="Date_Expired"),
		url(r'^GET_LIST_INVOICE/$',GET_LIST_INVOICE,name="GET_LIST_INVOICE"),
		url(r'^View_Invoice/(\d+)/$',View_Invoice,name="View_Invoice"),
		url(r'^GET_LIST_NOTE_CREDIT/(\d+)/$',GET_LIST_NOTE_CREDIT,name="GET_LIST_NOTE_CREDIT"),
		url(r'^CreditNote/(\d+)/(\d+)/$',CreditNote,name="CreditNote"),

		url(r'^SetPayment/$',SetPayment,name="SetPayment"),
		url(r'^Send_DIAN/$',Send_DIAN,name="Send_DIAN"),
	]