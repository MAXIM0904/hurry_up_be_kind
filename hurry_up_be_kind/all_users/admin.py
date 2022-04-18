from django.contrib import admin
from .models import Philantropist, Ward


class PhilantropistAdmin(admin.ModelAdmin):
    pass

class WardAdmin(admin.ModelAdmin):
    pass

admin.site.register(Philantropist, PhilantropistAdmin)
admin.site.register(Ward, WardAdmin)