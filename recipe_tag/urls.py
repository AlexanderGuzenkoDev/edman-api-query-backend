from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipeTags, name='recipeTag-list'),
    path('<int:pk>/', views.set_action, name='recipeTag-action'),
]