from django.contrib import admin
from .models import *

# Register your models here.
class CompaniesAdmin(admin.ModelAdmin): 
  prepopulated_fields = {"slug": ["company_name",]}
  def get_actions(self, request): 
    actions = super().get_actions(request) 
    if request.user.username[0].upper() != "J": 
      if "delete_selected" in actions: 
        del actions["delete_selected"] 
    return actions
  def __str__(self): 
    return self.company_name
  
admin.site.register(Company, CompaniesAdmin)