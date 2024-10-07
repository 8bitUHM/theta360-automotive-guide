# example/views.py
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Company

def index(request):
    companies = Company.objects.all()
    for company in companies:
        if company.company_name[0].islower():
            company.company_name = company.company_name.capitalize()
            company.save()

    companies = Company.objects.all().order_by('company_name')
    print(companies)
    return render(request, 'pages/home.html', {"companies": companies})

def company_detail(request, slug):
    company = get_object_or_404(Company, slug=slug)
    x_ready_percent = round((company.connect + company.take_picture + company.view)/3)
    return render(request, 'pages/company.html', {'company': company, 'x_ready_percent':x_ready_percent})