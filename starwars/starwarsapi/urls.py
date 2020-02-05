from rest_framework import routers
from .api import PlanetViewSet, CharacterViewSet, VehicleViewSet, StarshipViewSet, MovieViewSet, SpeciesViewSet, CharacterMovieViewSet

router = routers.DefaultRouter()
router.register('api/planets', PlanetViewSet, 'starwarsapi')
router.register('api/characters', CharacterViewSet, 'starwarsapi')
router.register('api/vehicles', VehicleViewSet, 'starwarsapi')
router.register('api/starships', StarshipViewSet, 'starwarsapi')
router.register('api/movies', MovieViewSet, 'starwarsapi')
router.register('api/species', SpeciesViewSet, 'starwarsapi')
router.register('api/charactermovies', CharacterMovieViewSet, 'starwarsapi')

urlpatterns = router.urls