from django.urls import path
from . import views

app_name = 'hello'

urlpatterns = [
   path('', views.myview),
   path('cookie', views.cookie),
   path('sessfun', views.sessfun),
]