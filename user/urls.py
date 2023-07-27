from django.conf.urls import url
from .views import *

urlpatterns=[
	url(r'^$',Login,name="Login"),
	url(r'^GET_LIST_EMPLOYEE/$',GET_LIST_EMPLOYEE,name="GET_LIST_EMPLOYEE"),
	url(r'^Add_Employee/$',Add_Employee,name="Add_Employee"),
	url(r'^LogOut/$',LogOut,name="LogOut"),
	url(r'^UPDATED_EMPLOYEE/$',UPDATED_EMPLOYEE,name="UPDATED_EMPLOYEE"),
	url(r'^CREATE_EMPLOYEE/$',CREATE_EMPLOYEE,name="CREATE_EMPLOYEE"),
	url(r'^DELETE_EMPLOYEE/$',DELETE_EMPLOYEE,name="DELETE_EMPLOYEE"),
	url(r'^Get_List_Close_Box/$',Get_List_Close_Box,name="Get_List_Close_Box"),
	url(r'^Edit/(\d+)/$',Edit,name="Edit"),
]