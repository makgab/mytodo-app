from django.contrib import admin

# Register your models here.

from .models import Todo, Type



admin.site.register(Todo)
admin.site.register(Type)
