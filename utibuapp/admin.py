from django.contrib import admin
from .models import Medication, Order, Statement

# Register your models here
admin.site.register(Medication)
admin.site.register(Order)
admin.site.register(Statement)