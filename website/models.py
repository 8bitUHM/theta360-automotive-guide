from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class File(models.Model): 
  bytes = models.TextField() 
  filename = models.CharField(max_length=255) 
  mimetype = models.CharField(max_length=50) 

  def __str__(self): 
    return self.filename

class Company(models.Model): 
  # Company details field
  company_name = models.CharField(max_length=100, help_text="Enter the company's name.") 
  tagline = models.CharField(max_length=255, help_text="Enter a tagline for the company.")
  details = models.TextField(help_text="Enter a detailed description of the company.")
  reference_link = models.URLField(max_length=200, default="", help_text="Enter the link to the company.")
  image = models.ImageField(upload_to='website.File/bytes/filename/mimetype', null=True, help_text="Upload an image of the company.") 
  reference_link_label = models.CharField(max_length=100, help_text="Enter the label for the reference link.")
  
  # Company data fields
  show_chart = models.BooleanField(default=False, help_text="Indicates if the chart should be shown.")
  connect = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(100)], help_text="Connection rating (max 100).")
  take_picture = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(100)], help_text="Rating for picture-taking feature (max 100).")
  view = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(100)], help_text="Rating for viewing feature (max 100).")
  opinion = models.TextField(help_text="Opinion on the company.")
  additional_details = models.TextField(help_text="Additional details about the company.")

  def __str__(self): 
    return self.company_name

  def delete(self, *args, **kwargs): 
    super(Company, self).delete(*args, **kwargs) 
    File.objects.filter(filename = self.image.name).delete()
