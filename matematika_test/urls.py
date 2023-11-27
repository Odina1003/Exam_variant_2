from django.urls import path
from .views import main, math

urlpatterns = [
    path('', main),
    path('tests/', math, name='math'),
]