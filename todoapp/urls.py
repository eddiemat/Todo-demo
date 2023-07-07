
from django.urls import path

from todoapp import views

urlpatterns=[
    path('', views.home, name='home'),
    path('forms/', views.forms, name='forms'),
    path('usingUserCreatedForm/', views.usingUserCreatedForm, name='usingUserCreatedForm'),
    path('usingModelForm/', views.usingModelForm, name='usingModelForm'),
    path('usingDjangoForm/', views.usingDjangoForm, name='usingDjangoForm'),
]