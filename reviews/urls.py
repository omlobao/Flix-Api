from django.urls import path
from . import views

urlpatterns = [
    path('', views.ReviewCreateListView.as_view(), name='review_create_list'),
    path('<int:id>/', views.ReviewRetrieveUpdateDestroyView.as_view(), name='review_retrieve_update_destroy'),
]