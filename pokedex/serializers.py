from rest_framework.serializers import ModelSerializer

from pokedex.models import Pokemon, Ability, Type


class PokemonModelSerializer(ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ('id', 'name', 'weight', 'gender', '_type', 'abilities')
