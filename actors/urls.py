from django.urls import path
from . import views

urlpatterns = [
    path('', views.ActorListCreateView.as_view(), name='actor_create_list'),
    path('<int:id>/', views.ActorRetrieveUpdateDestroyView.as_view(), name='actor_retrieve_update_destroy'),
    path('stats/', views.ActorStatsView.as_view(), name='actors-stats-view'),
]
