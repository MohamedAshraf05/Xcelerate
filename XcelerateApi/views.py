from django.shortcuts import render
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
)
from edu.models import Lectures , Speakers
from .serializers import SpeakerSerializer , LectureSerializer
# Create your views here.

# displaying all the data
class LectureApiView(ListAPIView):
    queryset = Lectures.objects.all()
    serializer_class = LectureSerializer

class DetailLecture(RetrieveAPIView):
    queryset = Lectures.objects.all()
    serializer_class = LectureSerializer
    lookup_field = 'pk'

class SpeakerApiView(ListAPIView):
    queryset = Speakers.objects.all()
    serializer_class = SpeakerSerializer

class DetailSpeaker(RetrieveAPIView):
    queryset = Speakers.objects.all()
    serializer_class = SpeakerSerializer
    lookup_field = 'pk'

