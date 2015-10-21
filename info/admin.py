from django.contrib import admin
from info.models import Detail


class DetailAdmin(admin.ModelAdmin):
    fields = ['name', 'create_dt']

admin.site.register(Detail, DetailAdmin)
