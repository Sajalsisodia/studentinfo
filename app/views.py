from django.shortcuts import render
from .models import Students
from .serializers import StudentsSerializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

# Create your views here.

def  student_details(request):
    stu = Students.objects.all()
    serializer = StudentsSerializers(stu,many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json') 
     
    