from django.urls import path
from coglivros.views import home

urlpatterns = [
    path('home/', home, name='home')
]