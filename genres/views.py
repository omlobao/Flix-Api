from .models import Genre
# pyrefly: ignore [missing-import]
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import GenreSerializer
from app.permissions import GlobalDefaultPermissions


class GenreCreateListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, GlobalDefaultPermissions]
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    
    
class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, GlobalDefaultPermissions]
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    lookup_field = 'id'

