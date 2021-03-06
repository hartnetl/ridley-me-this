from django.contrib import admin
from .models import Turtle, turtle_sponsor


class TurtleAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'name',
        'species',
        'turtle_id',
        'date_tagged',
        'location_tagged',
        'sponsored_status',
    )

    ordering = ('sponsored_status',)


class TurtleSponsor(admin.ModelAdmin):
    list_display = (
        'name',
        'sponsorship_start',
        'sponsorship_end',
        'sponsored_by',
    )


admin.site.register(Turtle, TurtleAdmin)
admin.site.register(turtle_sponsor, TurtleSponsor)
