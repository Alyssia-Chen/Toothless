from django.urls import path
from . import views

app_name = 'useraccounts'
from django.urls import include, path

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', include('classavails.urls')),
]