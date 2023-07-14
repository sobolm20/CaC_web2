from django.contrib import admin
from .models import food

class foodAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

# Register your models here.
admin.site.register(food)
