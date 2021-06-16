from django.views import generic
from .models import ClassAvails


class IndexView(generic.ListView):
    template_name = 'classavails/index.html'
    context_object_name = 'classavails_list'
    def get_queryset(self):
        """Return the all the class availabilities."""
        return ClassAvails.objects.all()