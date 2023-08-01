from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("<int:tpr>", views.fabric_by_number),
    path("<str:tpr>", views.fabric, name="fabric-type")
]
