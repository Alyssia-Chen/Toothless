from django.db.models.base import Model
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from .models import Choice, ClassAvails
from notes.models import Notes
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .filters import ClassAvailsFilter
import logging

logger = logging.getLogger()

def add_class(request):
    if request.method == 'POST':
        if request.POST.get('add'):
            choice=Choice()
            choice.course = ClassAvails.objects.get(pk=(request.POST.get('add')))
            choice.user= request.user
            choice.save()
            
            return redirect('classavails:search')

    else:
        return redirect('classavails:search')

class IndexView(generic.ListView):
    template_name = 'classavails/index.html'
    context_object_name = 'choices_list'
    model = Choice

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update({
            'notes_list': Notes.objects.all(),
        })
        return context

    def get_queryset(self):
        return Choice.objects.all()


class SearchView(generic.ListView):
    template_name = 'classavails/search.html'
    context_object_name = 'classavails_list'
    # model = ClassAvails
    logger.debug('on search page')

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

class DeleteChoiceView(generic.edit.DeleteView):
    template_name = 'classavails/deletechoice.html' # override default of classavails/classavails_confirm_delete.html
    model = Choice
    success_url = reverse_lazy('classavails:index')


class TestView(generic.ListView):
    template_name = 'classavails/test.html'
    model = Choice

    def get_queryset(self):
        return Choice.objects.all()