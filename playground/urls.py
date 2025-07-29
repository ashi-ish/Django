from django.urls import path
from . import views

# URL configuration for the playground app
urlpatterns = [
    path('say-hello/', views.say_hello),
]
