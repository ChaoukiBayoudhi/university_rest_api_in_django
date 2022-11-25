from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from university_app.models import Student,Group,Address
from .serializers import StudentSerializer,GroupSerializer,AddressSerializer
from django.http import JsonResponse
#@api_view['GET','POST'] #we can put more than one Http method

@api_view(['GET'])
def get_all_students(request):
    if request.method=='GET':
        students=Student.objects.all() #get all  students from the database
        if  not students: #or if len(students) ==0 or if bool(students): #if there is no student in the list 
            return Response(status=status.HTTP_204_NO_CONTENT)
        serializer=StudentSerializer(students,many=True) #convert student objects to json
        return Response(serializer.data,status=status.HTTP_200_OK)
    return JsonResponse({"message":"The method is not allowed"},status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['POST'])
def add_student(request):
    if request.method=='POST':
        student=StudentSerializer(data=request.data) #get the student object from the request after deserialization
        if student.is_valid(): #check if the student object is valid (all required fields are filled and fields data types and format are correct)
            student.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(student.errors,status=status.HTTP_400_BAD_REQUEST)
    return JsonResponse({"message":"The method is not allowed"},status=status.HTTP_405_METHOD_NOT_ALLOWED)
            
@api_view(['DELETE'])
def delete_student(request,id):
                   
        if request.method=='DELETE':
            try:
                student=Student.objects.get(pk=id)
                student.delete()
                return JsonResponse({"message": "the student has been successfuly removed."},status=status.HTTP_202_ACCEPTED)
            except Student.DoesNotExist: 
                return Response(status=status.HTTP_404_NOT_FOUND)       
            
        return JsonResponse({"message":"The method is not allowed"},status=status.HTTP_405_METHOD_NOT_ALLOWED)



#Bussiness Logic implementation for Group model
 
@api_view(['GET','POST'])
def get_all_or_add_group(request):
     if request.method=='GET':
         groups=Group.objects.all() #get all  groups from the database as a list of objects
         if len(groups)==0: # there is no group in the the database (the Group table is empty)
             return Response(status=status.HTTP_204_NO_CONTENT)
         serializer=GroupSerializer(groups,many=True) #convert group objects to json; many=True means that we have a list of objects
         return Response(serializer.data,status=status.HTTP_200_OK) #return the json data with status code 200 to say that everything is ok
     elif request.method=='POST':
         group=GroupSerializer(data=request.data) #get the group object from the request after deserialization
         if group.is_valid():
             result=Group.objects.filter(name=group.validated_data['name']) #check if the group name already exists in the database
             if result:
                return JsonResponse({"message":"This group name already exists"},status=status.HTTP_400_BAD_REQUEST)
             group.save()
             return Response(status=status.HTTP_201_CREATED)
         return Response(group.errors,status=status.HTTP_400_BAD_REQUEST)
     return JsonResponse({"message":"The method is not allowed"},status=status.HTTP_405_METHOD_NOT_ALLOWED)
 
@api_view(['GET','PUT','DELETE'])
def retreive_update_or_delete_group(request,id):
    if request.method=='GET':
        try:
            group=Group.objects.get(pk=id)
            serializer=GroupSerializer(group)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Group.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    elif request.method=='PUT':
       pass
    elif request.method=='DELETE':
        pass
    return JsonResponse({"message":"The method is not allowed"},status=status.HTTP_405_METHOD_NOT_ALLOWED)
