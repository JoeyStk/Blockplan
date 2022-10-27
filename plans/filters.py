import django_filters
from django_filters import CharFilter
from .models import Class, Plan, Week

class ClassFilter(django_filters.FilterSet):
    
    class Meta:
        model = Class
        fields = '__all__'
        exclude = ['name']