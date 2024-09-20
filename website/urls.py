# example/urls.py
from django.urls import path

from website.views import index, company_detail

urlpatterns = [
  path('', index, name='home'),
  path('company/<slug:slug>/', company_detail, name='company-detail'),
]