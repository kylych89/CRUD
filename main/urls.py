from django.urls import path

from .views import index, create_student, student_update, student_delete

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('create_student/', create_student, name='create_student'),
    path('update_student/<int:pk>/', student_update, name='update_student'),
    path('delete_student/<int:pk>/', student_delete, name='delete_student'),
]
