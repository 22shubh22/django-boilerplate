from django.urls import path, include
from .views import *

urlpatterns = [
    path("hello/", HelloView.as_view(), name='hello'),
]