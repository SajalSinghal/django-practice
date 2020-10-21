from django.contrib import admin
from . import models

# To change the admin ui properties so that we can define the new sequence here and register it with model
class MovieAdmin(admin.ModelAdmin):
    fields = ['release_year', 'length', 'movie']           # sequence of model fields in db

    search_fields = ['movie', 'release_year']              # to display search field with items to be searched related to a property

    list_filter = ['release_year', 'length', 'movie']      # to list the filters for easy filtering of data

    list_display = ['movie', 'release_year', 'length']     # to display the model properties in list form outside

    list_editable = ['length']                             # to edit the model properties outside for display only properties


# Register your models here.
admin.site.register(models.Movie, MovieAdmin)
admin.site.register(models.Customer)
