from rest_framework import serializers

from .models import Hero, UserProfile, CourseName

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = ('name', 'alias')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id','userName', 'password', 'successLogin', 'listCourses']

class CourseNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseName
        fields = ['courseName']