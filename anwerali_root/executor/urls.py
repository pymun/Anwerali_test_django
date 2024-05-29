from django.urls import path
from . import views

urlpatterns = [
    path('executor/', views.executor_page, name='executor_page')
]