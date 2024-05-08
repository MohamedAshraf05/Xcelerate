from django.contrib import admin
from .models import Lectures , Speakers
# Register your models here.
@admin.register(Lectures)
class LecturesAdmin(admin.ModelAdmin):
    list_display = ['title' , 'category' ,'status' , 'publish']

@admin.register(Speakers)
class SpeakersAdmin(admin.ModelAdmin):
    list_display = ['Name' , 'Job']