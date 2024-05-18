from django.urls import path
from .views import ClientListCreateView, ClientRetrieveUpdateDestroyView, ProjectCreateView, ProjectListView
from . import views

urlpatterns = [
    path('', ClientListCreateView.as_view(), name='client-list-create'),
    path('clients/<int:pk>/', ClientRetrieveUpdateDestroyView.as_view(), name='client-detail'),
    path('projects/', ProjectListView.as_view(), name='project-list'),
    path('projects/create/', ProjectCreateView.as_view(), name='project-create'),
    path('projects/<int:pk>/', views.ProjectDeleteView.as_view(), name='project-delete'),
]
