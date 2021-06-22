import django_filters
from .models import ClassAvails


class ClassAvailsFilter(django_filters.FilterSet):

    class Meta:
        model = ClassAvails
        fields = {
            'CRN': ['icontains'],
            'course': ['icontains'],
            'title': ['icontains'],
        }