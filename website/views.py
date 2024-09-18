# example/views.py
from django.shortcuts import render
from .models import Company

def index(request):
    companies = Company.objects.all()
    for company in companies:
        if company.company_name[0].islower():
            company.company_name = company.company_name.capitalize()
            company.save()

    companies = Company.objects.all().order_by('company_name')
    print(companies)
    return render(request, 'pages/home.html', {"company": companies})

