from django.shortcuts import render
from . models import ExecutorModel

# Create your views here.
def executor_page(request):
    executor_list = ExecutorModel.objects.all()
    return render(request, './executor.html', 
                  {'executor_list': executor_list})