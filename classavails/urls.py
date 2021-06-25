from django.urls import path
from . import views

app_name = 'classavails'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('add_class', views.add_class, name='add_class'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('new/', views.CreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.UpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.DeleteView.as_view(), name='delete'),
]