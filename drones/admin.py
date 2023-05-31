from django.contrib import admin

# Register your models here.
from .models import Drone, BatteryStatus, DroneStatusMovement


class DroneAdmin(admin.ModelAdmin):
    pass


class BatteryStatusAdmin(admin.ModelAdmin):
    pass


class DroneStatusMovementAdmin(admin.ModelAdmin):
    pass


admin.site.register(Drone, DroneAdmin)
admin.site.register(BatteryStatus, BatteryStatusAdmin)
admin.site.register(DroneStatusMovement, DroneStatusMovementAdmin)
