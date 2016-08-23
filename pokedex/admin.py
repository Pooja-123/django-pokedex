from django.contrib import admin

from pokedex.models import Pokemon, Type, Ability


admin.site.register(Pokemon)
admin.site.register(Type)
admin.site.register(Ability)
