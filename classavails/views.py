from django.views import generic
from django.urls import reverse_lazy
from .models import ClassAvails
from notes.models import Notes
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .filters import ClassAvailsFilter

class IndexView(generic.ListView):
    template_name = 'classavails/index.html'
    context_object_name = 'notes_list'
#user.is_authenticated
#    if :
 #       logged_in = true
  #  else:
   #     logged_in = false

    def get_queryset(self):
        """Return all the Notes."""
        return Notes.objects.all()

class SearchView(generic.ListView):
    template_name = 'classavails/search.html'
    context_object_name = 'classavails_list'
    # model = ClassAvails

    def get_queryset(self):
        """Return the all the class availabilities."""
        return ClassAvails.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ClassAvailsFilter(self.request.GET, queryset = self.get_queryset())
        return context

@method_decorator(login_required, name='dispatch')
class CreateView(generic.edit.CreateView):
    template_name = 'classavails/create.html'
    model = Notes
    fields = ['note', 'author']
    success_url = reverse_lazy('classavails:index')

class UpdateView(generic.edit.UpdateView):
    template_name = 'classavails/update.html'
    model = Notes
    fields = ['note']
    success_url = reverse_lazy('classavails:index')

class DeleteView(generic.edit.DeleteView):
    template_name = 'classavails/delete.html' # override default of classavails/classavails_confirm_delete.html
    model = Notes
    success_url = reverse_lazy('classavails:index')
    