from django.urls import path
from .views import lesson_list, lesson_detail

urlpatterns = [
    path('', lesson_list, name='lesson_list'),
    path('<int:pk>/', lesson_detail, name='lesson_detail'),  
]
