from django.contrib import admin
from .models import Todo

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
    list_display = ['id', 'user', 'title', 'important', 'created_at']
