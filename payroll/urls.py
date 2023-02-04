from django.conf.urls import url
from .views import *

urlpatterns=[
	url(r'^Create_Payroll/$',Create_Payroll,name="Create_Payroll"),
]