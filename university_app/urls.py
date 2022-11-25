from django.urls import include,path
from rest_framework import routers
from . import views
#urls using ModelViewSet
# from university_app.viewsets import AddressViewSet, GroupViewSet, StudentViewSet
# router=routers.DefaultRouter() #get the default router object defined in rest_framework
# #add router for each viewset (StudentViewest, GroupViewSet, AddressViewSet) to the router object
# router.register(r'students',StudentViewSet) 
# #each time we use the path '/students' in the url, 
# #the StudentViewSet will be called
# #the prefix r is used to indicate that the string is a raw string (not interpret the backslash as an escape character)
# router.register(r'groups',GroupViewSet)
# router.register(r'addresses',AddressViewSet)

# #add the router to the urlpatterns
# urlpatterns = [
#     path('', include(router.urls)),
# ]

urlpatterns = [
    path(r'all/',views.get_all_students),
    path(r'add/',views.add_student),
    path(r'delete/',views.delete_student),
]
