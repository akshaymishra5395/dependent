from django.urls import path
from .views import base_view,getfloors
app_name='takelog'

urlpatterns = [
    path('', base_view),
    path('ajax/getfloors/',getfloors,name='getfloors')
]
