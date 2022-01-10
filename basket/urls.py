from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_basket, name='view_basket'),
    path('addmerch/<item_id>/', views.add_merch_to_basket, name='add_merch_to_basket'),
]
