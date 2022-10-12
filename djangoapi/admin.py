from django.contrib import admin
from .models import something

@admin.register(something)

class admin_something(admin.ModelAdmin):
    list_display = ['id', 'first', 'second']