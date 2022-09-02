from django.urls import path

from .views import *


urlpatterns = [
    path('', rooms_view,name='rooms'),
]
