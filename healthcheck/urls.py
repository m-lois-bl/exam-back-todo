# healthcheck/urls.py
from django.urls import path
from .views import health_check, trigger_error

urlpatterns = [
    path("", health_check, name="health"),
    path('sentry-debug/', trigger_error, name='trigger_error'), 
]