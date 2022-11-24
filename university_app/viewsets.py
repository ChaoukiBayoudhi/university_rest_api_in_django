from university_app.serializers import AddressSerializer, GroupSerializer, StudentSerializer
from rest_framework import viewsets
from .models import Student, Group, Address

class StudentViewSet(viewsets.ModelViewSet):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    http_method_name = ['get', 'post', 'put', 'delete','patch']
    
class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    http_method_name = ['get', 'post', 'put', 'delete','patch']

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    http_method_name = ['get', 'post', 'put', 'delete','patch'] 