from django.contrib import admin
from .models import Barber, Service, Appointment, UserProfile

# Register your models here.
admin.site.register(Barber)
admin.site.register(Service)
admin.site.register(Appointment)
admin.site.register(UserProfile)

