from django.contrib import admin
from .models import Activity, Effort

models = [Activity, Effort]
admin.site.register(models)
