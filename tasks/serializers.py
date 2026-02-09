from rest_framework import serializers
from .models import Category, Task


class CategorySerializer(serializers.ModelSerializer):
    """
    Classe de gestion de la sérialisation d'une entité de Category au format JSON.
    """
    class Meta:
        model = Category
        fields = '__all__'
        extra_kwargs = {
            'name': {'error_messages': {'unique': 'Une catégorie ayant le même nom existe déjà.', 'max_length': 'Le nom de la catégorie ne peut excéder 100 caractères.','blank': 'Le nom de la catégorie doit être renseigné.'}}
        }
        read_only_fields  = ['id']
    
    def validate_name(self, value):
        """
        Vérifie que le nom de la catégorie fait plus de trois caractères et est bien unique (insensibilité à la casse)
        """
        if len(value.strip()) < 3 :
            raise serializers.ValidationError("Le nom de la catégorie doit comporter au moins trois caractères.")
        categoryWithSameName = Category.objects.filter(name__iexact=value)
        if self.instance:
            categoryWithSameName.exclude(pk=self.instance.id)
        if categoryWithSameName.exists():
            raise serializers.ValidationError("Le nom de la catégorie doit être unique.")
        return value


class TaskSerializer(serializers.ModelSerializer):
    """
    Classe de gestion de la sérialisation d'une entité de Task au format JSON.
    """
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), 
        error_messages = {
            'required': 'La catégorie doit être renseignée',
            'does_not_exist': 'Catégorie invalide'
        }   
    )
    class Meta:
        model = Task
        fields = '__all__'
        extra_kwargs = {
            'description': {'error_messages': {'max_length': 'La description ne doit pas dépasser 2000 caractères.', 'blank': 'Le description de la tâche doit être renseignée.'}}
        }
        read_only_fields = ['id', 'created_at']

    def validate_description(self, value):
        """
        Vérifie que la description comporte au moins trois caractères.
        """
        if len(value.strip()) < 3 :
            raise serializers.ValidationError("La description doit comporter au moins trois caractères.")
        return value

