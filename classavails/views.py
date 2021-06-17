from django.views import generic
from .models import ClassAvails
from notes.models import Notes

class IndexView(generic.ListView):
    template_name = 'classavails/index.html'
    context_object_name = 'notes_list'
    def get_queryset(self):
        """Return all the Notes."""
        return Notes.objects.all()

class SearchView(generic.ListView):
    template_name = 'classavails/search.html'
    context_object_name = 'classavails_list'
    def get_queryset(self):
        """Return the all the class availabilities."""
        return ClassAvails.objects.all()