from django.urls import path
from . import views

urlpatterns = [
    path('', views.about_page, name='info'),
    path('learn/', views.learn_more, name='learn'),
]
