from django.contrib import admin
from . import models

@admin.register(models.Ticket)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'fullname', 'mobile','create_at',)
