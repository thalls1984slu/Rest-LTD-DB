from django.contrib import admin

from.models import YearlySchedule

# Register your models here.
@admin.register(YearlySchedule)
class YearlyScheduleAdmin(admin.ModelAdmin):
    list_display = ('job', 'year', 'scheduled_date')
    list_filter = ('year', 'job')