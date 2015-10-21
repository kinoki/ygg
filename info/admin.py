from django.contrib import admin
from info.models import Detail


class DetailAdmin(admin.ModelAdmin):
    model = Detail
    list_display = ('name', 'create_dt')
    fields = ['name']
    readonly_fields = ('create_dt',)

admin.site.register(Detail, DetailAdmin)
