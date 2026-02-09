from django.db import models
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower

# Create your models here.
class Category(models.Model):
    """
    Classe représentant une catégorie de tâche.
    """
    name = models.CharField(
        max_length=100, 
        unique=True, 
        error_messages={
            'max_length': 'Le nom de la catégorie ne peut excéder 100 caractères.',
            'blank': 'Le nom de la catégorie doit être renseigné.'
            }
    )
    class Meta: 
        constraints = [
            UniqueConstraint(
                Lower('name'),
                name='unique_name_ci',
                violation_error_message='Une catégorie ayant le même nom existe déjà.' 
            ) 
        ]

    def __str__(self):
        return self.name
    
class Task(models.Model):
    description = models.TextField(
        max_length=2000,
        error_messages={
            'max_length': 'La description ne doit pas dépasser 2000 caractères.',
            'blank': 'Le description de la tâche doit être complétée.'
        }
    )
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        error_messages={
            'invalid': 'Catégorie inexistante.'
        }   
    )

    def __str__(self):
        return f"[{self.category.name}] : {self.description}. Statut : {"Réalisée" if self.is_completed else "À faire"}."