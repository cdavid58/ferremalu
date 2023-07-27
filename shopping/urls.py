from django.conf.urls import url
from .views import *

urlpatterns=[
	url(r'^Create_Shopping/$',Create_Shopping,name="Create_Shopping"),
	url(r'^Get_Product/$',Get_Product,name="Get_Product"),
	url(r'^Save_Shopping/$',Save_Shopping,name="Save_Shopping"),
	url(r'^Test/$',Test,name="Test"),
	url(r'^QUERY_SHOPPINGS/$',QUERY_SHOPPINGS,name="QUERY_SHOPPINGS"),
]