from django.conf.urls import url
from .views import *

urlpatterns=[
		url(r'^Get_Wallet_POS/$',Get_Wallet_POS,name="Get_Wallet_POS"),
		url(r'^Cancelled/$',Cancelled,name="Cancelled"),
	]