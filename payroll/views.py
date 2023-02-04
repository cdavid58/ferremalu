from django.shortcuts import render

def Create_Payroll(request):
	return render(request,'payroll/create_payroll.html')
