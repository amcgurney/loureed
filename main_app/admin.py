from django.contrib import admin
from .models import Songs # import the Artist model from models.py
# Register your models here.

admin.site.register(Songs) # this line will add the model to the admin panel
