from django.contrib import admin

from plan.models import Plan, TimeUntilDone


@admin.register(TimeUntilDone)
class TimeUtilDoneAdmin(admin.ModelAdmin):
    list_display = ('id','name')

@admin.register(Plan)
class PlansAdmin(admin.ModelAdmin):
    list_display = ('id','title','slug','author')
    prepopulated_fields = {'slug':('title',)}

