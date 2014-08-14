from django.contrib import admin
from nba.models import Player

class PlayerAdmin(admin.ModelAdmin):
	list_display = ('full_name', 'jersey', 'position', 'age', \
		'pick', 'height', 'weight', 'school', 'country', 'birthdate', 'is_active')
	# list_display_links = ('first_name', 'last_name')
	list_filter = ('is_active', 'position', 'pick')
	search_fields = ['first_name', 'last_name']

admin.site.register(Player, PlayerAdmin)