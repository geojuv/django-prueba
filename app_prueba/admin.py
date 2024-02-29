from django.contrib import admin
from django.contrib.gis.admin import GISModelAdmin
from .models import Topic

# Register your models here.


# admin.site.register(Topic)

class CustomGeodmin(GISModelAdmin): 
    gis_widget_kwargs = { 'attrs': 
                        { 'default_lon':100, 'default_lat': 50, 'default_zoom': 11,
                        }
                        }                       

@admin.register(Topic) 
class EnclosureAdmin(CustomGeodmin):
    pass

# @admin.register(Topic)
# class departamentoAdmin(GISModelAdmin):
#     list_display = ('text', 'location',)
#         # ---- NEW ----
#     gis_widget_kwargs = {
#             'attrs': {
#                 'default_zoom': 8,
#                 'default_lat': -16,
#                 'default_lon': -67,
#             },
#         }
    
# @admin.register(Topic)
# class EnclosureAdmin(GISModelAdmin):
#     gis_widget_kwargs = {
#         'attrs': {
#             'default_lon': 40.383546,
#             'default_lat': -111.774973,
#         }
#     }