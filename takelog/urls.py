from django.urls import path
from .views import getfloors
app_name='takelog'

urlpatterns = [
    path('ajax/getfloors/',getfloors,name='getfloors')
]
