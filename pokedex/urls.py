from rest_framework import routers

from pokedex.views import PokemonModelViewSet


router = routers.DefaultRouter()

router.register('pokemon', PokemonModelViewSet)

urlpatterns = router.urls
