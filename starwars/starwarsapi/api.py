from starwarsapi.models import Planet, Species, Character, Vehicle, Starship, Movie, CharacterMovie
from rest_framework import viewsets, permissions
from .serializers import PlanetSerializer, CharacterSerializer, SpeciesSerializer, VehicleSerializer, StarshipSerializer, MovieSerializer, CharacterMovieSerializer

class PlanetViewSet(viewsets.ModelViewSet):
    queryset = Planet.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PlanetSerializer

class SpeciesViewSet(viewsets.ModelViewSet):
    queryset = Species.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SpeciesSerializer

class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CharacterSerializer

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = VehicleSerializer

class StarshipViewSet(viewsets.ModelViewSet):
    queryset = Starship.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = StarshipSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = MovieSerializer

class CharacterMovieViewSet(viewsets.ModelViewSet):
    queryset = CharacterMovie.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CharacterMovieSerializer