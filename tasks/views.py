from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Category, Task
from .serializers import CategorySerializer, TaskSerializer

# Create your views here.
class CategoryViewset(viewsets.ModelViewSet):
    """
    Permet de :
    - GET /api/categories/ : récupérer la liste de toutes les catégories
    - POST /api/categories/ : ajouter une nouvelle catégorie
    - GET /api/categories/{id}/ : récupérer une catégorie à partir de son identifiant
    - PUT /api/categories/{id}/ : modifier une catégorie
    - PATCH /api/categories/{id}/ : modifier un attribut d'une catégorie
    - DELETE /api/categories/{id}/ : supprimer une catégorie
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = None

class TaskViewset(viewsets.ModelViewSet):
    """
    Permet de :
    - GET /api/tasks/ : récupérer la liste de toutes les tâches ordonnées par défaut par date de création décroissante
    - POST /api/tasks/ : ajouter une nouvelle tâche
    - GET /api/tasks/{id}/ : récupérer une tâche à partir de son identifiant
    - PUT /api/tasks/{id}/ : modifier une tâche
    - PATCH /api/tasks/{id}/ : modifier un attribut d'une tâche
    - DELETE /api/tasks/{id}/ : supprimer une tâche
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    ordering_fields = ['created_at']
    ordering = ['-created_at']
    filterset_fields = ['category', 'is_completed']