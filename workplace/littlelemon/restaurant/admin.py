from django.contrib import admin
from .models import Menu
# Register your models here.
admin.site.register(Menu)
#making migrations
#python3 manage.py makemigrations
#python3 manage.py migrate