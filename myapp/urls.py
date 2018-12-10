from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('register',views.modal_detail,name='modals'),
    ]