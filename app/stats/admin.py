from django.contrib import admin
from stats.models import Record


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ('name', 'link', 'views', 'release_date',
                    'stats_date', 'is_active', 'is_deleted')
    fields = ['name', 'link', 'is_active', ]
    ordering = ('-date_created',)
    search_fields = ('name', 'link',)
