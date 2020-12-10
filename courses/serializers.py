from rest_framework import serializers
from .models import Course

# create a course serializer
class CourseSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Course
		fields = ('id', 'url', 'name', 'language', 'price')