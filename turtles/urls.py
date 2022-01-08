from django.urls import path
from . import views

urlpatterns = [
    path('', views.turtles, name='turtles'),
    path('<turtle_id>', views.turtle_detail, name='turtle_detail'),
]
