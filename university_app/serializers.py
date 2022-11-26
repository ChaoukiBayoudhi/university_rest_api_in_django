from rest_framework import serializers
from .models import Student, Group, Address,Module

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__' #serializes all fields
        #fields=('id','name','familyName','group') #serializes only these fields
        
class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model=Group
        fields='__all__' #serializes all fields
class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model= Address
        fields='__all__' #serializes all fields
        
class ModuleSerializer(serializers.ModelSerializer):
    #Serialization of the many to many relationship between Module and Group
    studies=GroupSerializer(many=True,
                            read_only=True,
                            required=False)
    class Meta:
        model= Module
        fields='__all__' #serializes all fields
        