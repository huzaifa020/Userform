from django.contrib import admin
from form.models import *
# Register your models here.
class formadmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'password']
admin.site.register(form, formadmin)