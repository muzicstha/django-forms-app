
from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact),
    path('snipper', views.snipper_detail)
]