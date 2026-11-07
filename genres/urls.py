from django.urls import path
from . import views

urlpatterns = [
    path('', views.GenreCreateListView.as_view(), name='genre_create_list'),
    path('<int:id>/', views.GenreRetrieveUpdateDestroyView.as_view(), name='genre_retrieve_update_destroy'),
]