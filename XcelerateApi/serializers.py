from rest_framework import serializers
from edu.models import Lectures , Speakers



class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lectures
        fields = ("title" , "lecture" , "author")

class SpeakerSerializer(serializers.ModelSerializer):
    class Meta : 
        model = Speakers
        fields = ('Name' , "Job")