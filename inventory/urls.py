from django.conf.urls import url
from .views import *

urlpatterns=[
		url(r'^List_Inventory/$',List_Inventory,name="List_Inventory"),
		url(r'^Add_Product/$',Add_Product,name="Add_Product"),
		url(r'^Save_Product/$',Save_Product,name="Save_Product"),
		url(r'^UPDATED_PRODUCT/$',UPDATED_PRODUCT,name="UPDATED_PRODUCT"),
		url(r'^Montage_Inventory/$',Montage_Inventory,name="Montage_Inventory"),
		url(r'^DELETE_PRODUCT/$',DELETE_PRODUCT,name="DELETE_PRODUCT"),
		url(r'^Edit_Product/(\d+)/$',Edit_Product,name="Edit_Product"),
	]