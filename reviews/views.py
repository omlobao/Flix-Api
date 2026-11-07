from django.db.models import QuerySet
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from rest_framework import generics, views
from reviews.models import Review
from .serializers import ReviewSerializer
from app.permissions import GlobalDefaultPermissions



class ReviewCreateListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, GlobalDefaultPermissions]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, GlobalDefaultPermissions]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = 'id'
    
    

class ReviewStatsView(views.APIView):
    permission_classes = [IsAuthenticated, GlobalDefaultPermissions]
    queryset = Review.objects.all()

    def get(self, request):
        total_reviews=self.queryset.count()

