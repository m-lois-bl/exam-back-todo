from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewset, TaskViewset

router = DefaultRouter()
router.register(r"categories", CategoryViewset, basename='category')
router.register(r"tasks", TaskViewset, basename='task')

urlpatterns = [
    path("", include(router.urls)),
]