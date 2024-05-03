from django.contrib import admin
from .models import Lectures
# Register your models here.
@admin.register(Lectures)
class LecturesAdmin(admin.ModelAdmin):
    list_display = ['title' , 'category' ,'status' , 'publish']
