from django.contrib import admin
from .models import User

models = [User]
admin.site.register(models)
