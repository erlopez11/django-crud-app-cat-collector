from django.urls import path
from . import views 

#this is a python list
urlpatterns = [
    path('', views.home, name='home'), # route to homepage
    #path('about/...')
    path('about/', views.about, name='about'),
    path('cats/', views.cat_index, name='cat-index'),
    path('cats/<int:cat_id>', views.cat_detail, name='cat-detail'),
    #path('create/...')
    
]
