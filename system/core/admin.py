from django.contrib import admin
from .models import Farmer, Vehicle, Driver, Job, Revenue

admin.site.register(Farmer)
admin.site.register(Vehicle)
admin.site.register(Driver)
admin.site.register(Job)
admin.site.register(Revenue)