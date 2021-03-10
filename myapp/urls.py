from django.urls import path
from .views import *

urlpatterns = [
    path('', homepage, name='homepage'),
    path('update/<str:pk>', update, name='update'),
    path('delete/<str:pk>', delete, name='delete'),
]
