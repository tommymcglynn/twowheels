from django.contrib import admin

from web.models import Bike, BikeStyle, BikeMake, BikeFamily, BikeModel, BikePart


class BikeAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'name', 'created', 'modified')
    readonly_fields = ('image_tag', 'created', 'modified')
    fieldsets = [
        (None,                  {'fields': ['name']}),
        ('Date',                {'fields': ['created', 'modified']}),
        ('Image',               {'fields': ['image_tag', 'image_url', 'source_url']}),
        ('Indices',             {'fields': ['models', 'styles', 'parts']}),
    ]

admin.site.register(Bike, BikeAdmin)
admin.site.register(BikeStyle)
admin.site.register(BikeMake)
admin.site.register(BikeFamily)
admin.site.register(BikeModel)
admin.site.register(BikePart)
