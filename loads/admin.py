from django.contrib import admin
from .models import Load, LoadStatusMovement
# Register your models here.


class LoadAdmin(admin.ModelAdmin):
    pass


class LoadStatusMovementAdmin(admin.ModelAdmin):
    pass


admin.site.register(Load, LoadAdmin)
admin.site.register(LoadStatusMovement, LoadStatusMovementAdmin)
