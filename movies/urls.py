from django.urls import path
from . import views

urlpatterns = [
    path('', views.MovieCreateListView.as_view(), name='movie_create_list'),
    path('<int:id>/', views.MovieRetrieveUpdateDestroyView.as_view(), name='movie_retrieve_update_destroy'),
    path('stats/', views.MovieStatsView.as_view(), name='movie-stats-view'),
]
