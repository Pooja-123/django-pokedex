from rest_framework import routers

from pokedex.views import PokemonModelViewSet


router = routers.SimpleRouter()

router.register('pokemon', PokemonModelViewSet)

urlpatterns = router.urls
print urlpatterns
