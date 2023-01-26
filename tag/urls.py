from django.urls import path
from . import views

urlpatterns = [
    path('', views.tags, name='tag-list'),
    path('<int:pk>/', views.set_action, name='tag-action'),
]