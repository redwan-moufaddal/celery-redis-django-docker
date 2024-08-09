from django.urls import path
from marketing import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('submit_task/', views.submit_task, name='submit_task'),
    path('task_status/<str:task_id>/', views.check_task_status, name='check_task_status'),
]
