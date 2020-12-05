from django.contrib import admin
from .models import service

# Register your models here.

class serviceAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

admin.site.register(service,serviceAdmin)