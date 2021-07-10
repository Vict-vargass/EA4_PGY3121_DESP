from django.urls import path
from rest_api.views import obras_api, obra_api
from rest_api.viewsLogin import login

urlpatterns = [
    path('obras-api', obras_api, name='obras'),
    path('obra/<pk>', obra_api, name='obra'),
    path('login', login, name='login'),
]