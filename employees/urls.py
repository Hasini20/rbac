from django.urls import include, path 
from employees.views import EmployeeCreate, EmployeeList, EmployeeDetail, EmployeeUpdate, EmployeeDelete
 
urlpatterns=[
    path('create/', EmployeeCreate.as_view(), name='create-employee'),
    path('', EmployeeList.as_view()),
    path('<int:pk>/', EmployeeDetail.as_view(), name='retrieve-employee'),
    path('update/<int:pk>', EmployeeUpdate.as_view(), name='update-employee'),
    path('delete/<int:pk>/', EmployeeDelete.as_view(), name='delete-employee')
]

    


