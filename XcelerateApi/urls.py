from django.urls import path
from .views import SpeakerApiView , DetailSpeaker , LectureApiView , DetailLecture



urlpatterns = [
    path('speakers/' , SpeakerApiView.as_view() , name='Speaker-api'),
    path('speaker/<int:pk>/' , DetailSpeaker.as_view() , name='Retrieve-speaker' ),
    path('Lectures/' , LectureApiView.as_view() , name='Lectures-api'),
    path('Lecture/<int:pk>/' , DetailLecture.as_view() , name='Retrieve-lecture'),
]


