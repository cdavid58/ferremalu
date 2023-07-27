from django.conf.urls import url
from .views import *

urlpatterns=[
		url(r'^Invoice/$',Invoice,name="Invoice"),
	]