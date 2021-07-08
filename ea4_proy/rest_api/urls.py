from django.urls import path
from rest_api.views import obra_api

urlpatterns = [
    path('obra-api', obra_api, name='obra'),
]