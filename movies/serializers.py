from genres.serializers import GenreSerializer
from actors.serializers import ActorSerializer
from rest_framework import serializers
from movies.models import Movie
from django.db.models import Avg



class MovieSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True)
    genre = GenreSerializer()
    rate = serializers.SerializerMethodField(read_only=True)
    formatted_duration = serializers.ReadOnlyField()

    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'actors', 'release_date', 'rate', 'resume']

    def get_rate(self, obj):

        rate = obj.reviews.aggregate(Avg('stars')).get('stars__avg')
        if rate:
            return round(rate, 1)
        return None
        # reviews = obj.reviews.all()
        
        # if reviews.exists():
        #     sum_reviews = 0
        #     for review in reviews:
        #         sum_reviews += review.stars
        #     return round(sum_reviews / reviews.count(), 1)
        
        # return None

    def validate_release_date(self, value):
        if value and value.year < 1990:
            raise serializers.ValidationError('A data de lançamento não pode ser anterior a 1990')
        return value

    def validate_resume(self, value):
        if value and len(value) > 200:
            raise serializers.ValidationError('Resumo não pode exceder 200 caracteres')
        return value

    def validate_duration(self, value):
        if value and value <= 30:
            raise serializers.ValidationError('A duração mínima do filme é de 30 minutos para ser aceita')
        return value



class MovieListDetailSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True)
    genre = GenreSerializer()
    rate = serializers.SerializerMethodField(read_only=True)
    formatted_duration = serializers.ReadOnlyField()


    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'actors', 'release_date', 'rate', 'formatted_duration', 'resume']


    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars')).get('stars__avg')
        if rate:
            return round(rate, 1)
        return None

