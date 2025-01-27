from django.contrib import admin
from .models import Todoitem

@admin.register(Todoitem)
class TodoitmeAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'completed', 'created_at']


# admin.site.register(Todoitem)
