from django.urls import path
from . import views 

#this is a python list
urlpatterns = [
    path('', views.home, name='home'), # route to homepage
    #path('about/...')
    path('about/', views.about, name='about'),
    #path('create/...')
]
