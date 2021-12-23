from django.contrib import admin
from .models import Category, Merch, Donate


class MerchAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
        'rating',
        'image',
    )

    ordering = ('rating',)


class DonateAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
    )

    ordering = ('price',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Merch, MerchAdmin)
admin.site.register(Donate, DonateAdmin)
