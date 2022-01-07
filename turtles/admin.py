from django.contrib import admin
from .models import Turtles, turtle_sponsor

admin.site.register(Turtles)
admin.site.register(turtle_sponsor)

class TurtlesAdmin(admin.ModelAdmin):
    list_display = (
        'title'
        'name',
        'speies',
        'turtle_id',
        'date_tagged',
        'location_tagged',
        'sponsored_status',
    )

    ordering = ('species',)


class TurtleSponsor(admin.ModelAdmin):
    list_display = (
        'name',
        'sponsorship_start',
        'sponsorship_end',
        'sponsored_by',
    )



