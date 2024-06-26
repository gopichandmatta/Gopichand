from django.urls import path
from .views import DepartmentListCreate, DepartmentRetriveUpdateDestroy, EmployeeListCreate, EmployeeRetrieUpdateDestroy

urlpatterns = [
    path('department/', DepartmentListCreate.as_view(), name='department-list-create'),
    path('department/<int:pk>/', DepartmentRetriveUpdateDestroy.as_view(), name='department-details'),
    path('employee/', EmployeeListCreate.as_view(), name='employee-list-create'),
    path('employee/<int:pk>/', EmployeeRetrieUpdateDestroy.as_view(), name='employee - details'),

]
