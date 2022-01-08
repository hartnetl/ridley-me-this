from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_merch, name='merch'),
    path('<merch_id>', views.merch_detail, name='merch_detail'),
]
