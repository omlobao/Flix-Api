from django.db.models import Count
from rest_framework import generics, status, views, response
from rest_framework.permissions import IsAuthenticated

from app.permissions import GlobalDefaultPermissions
from .models import Actor
from .serializers import ActorSerializer


class ActorListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, GlobalDefaultPermissions]
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ActorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, GlobalDefaultPermissions]
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ActorStatsView(views.APIView):
    permission_classes = [IsAuthenticated, GlobalDefaultPermissions]
    queryset = Actor.objects.all()

    def get(self, request):
        total_actors = self.queryset.count()
        actors_by_nationality = self.queryset.values('nationality').annotate(total=Count('id'))

        total_by_nationality = {
            item['nationality'] or 'Nacionalidade não informada': item['total']
            for item in actors_by_nationality
        }

        return response.Response(
            data={
                'total_actors': total_actors,
                'total_by_nationality': total_by_nationality,
            },
            status=status.HTTP_200_OK,
        )