from django.urls import path
from . import views
from .views import *

app_name = 'Edu'

urlpatterns = [
    path('' , views.home , name='home'),
    path('logout/', views.logout ,name='logout'),
    path('login/' , CustomerLoginView.as_view() , name='login'),
    path('register/', CustomerRegisterView.as_view() , name='register'),
    path('lectures/<int:pk>/', LecDetails.as_view() , name='lecture'),
    path('lectures/',ScheduleView.as_view() , name='schedule'),
]