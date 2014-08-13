from django.contrib import admin
from nba.models import Player

class PlayerAdmin(admin.ModelAdmin):
	list_display = ('full_name', 'birthdate', 'school', 'country')

admin.site.register(Player, PlayerAdmin)