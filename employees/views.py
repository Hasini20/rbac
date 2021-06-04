from django.shortcuts import render

# Create your views here.
from employees.models import Employee
from rest_framework import generics 
from rest_framework import status
from employees.serializers  import EmployeeSerializer


class EmployeeCreate(generics.CreateAPIView):
    # API endpoin that allows creation of a new employee
        queryset = Employee.objects.all(),
        serializer_class=EmployeeSerializer

class EmployeeList(generics.ListAPIView):
    #API endpoint that allows employee to be viewed.
        queryset = Employee.objects.all(),
        serializer_class=EmployeeSerializer

class EmployeeDetail(generics.RetrieveAPIView):
    #API endpoint that returns a single employee by pk.
        queryset = Employee.objects.all(),
        serializer_class=EmployeeSerializer

class EmployeeUpdate(generics.RetrieveUpdateAPIView):
    #API endpoint that allows a employee record to be updated..
        queryset = Employee.objects.all(),
        serializer_class=EmployeeSerializer

class EmployeeDelete(generics.RetrieveDestroyAPIView):
    #API endpoint that allows a employee record to be deleted.
        queryset = Employee.objects.all(),
        serializer_class=EmployeeSerializer

