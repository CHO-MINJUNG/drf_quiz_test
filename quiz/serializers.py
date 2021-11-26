from rest_framework import serializers
from .models import Quiz

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ('title', 'body', 'answer')
        # json 데이터로 변환해주는 시리얼라이저 완성