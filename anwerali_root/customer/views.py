from django.shortcuts import render
from . models import CustomerModel


# Create your views here.
def customer_page(request):
    customer_list = CustomerModel.objects.all()
    return render(request, './index.html', {'customer_list': customer_list})