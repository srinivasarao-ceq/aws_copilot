from rest_framework import serializers
from .models import Student
class Studentserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Student
        fields='__all__'
        # fields=("stu_id","stu_name")s