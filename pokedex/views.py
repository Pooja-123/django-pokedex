from rest_framework.viewsets import ModelViewSet

from pokedex.serializers import PokemonModelSerializer
from pokedex.models import Pokemon


class PokemonModelViewSet(ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonModelSerializer
