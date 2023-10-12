from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver

class Barber(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='barber_photos/', blank=True, null=True)
    profile_text = models.TextField(blank=True, null=True)
    services_offered = models.ManyToManyField('Service', blank=True)

    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=100)
    duration_minutes = models.PositiveIntegerField(default=30)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.name} {self.duration_minutes} Min ${self.price}"

class Appointment(models.Model):
    barber = models.ForeignKey(Barber, on_delete=models.CASCADE)
    services = models.ManyToManyField(Service)
    appointment_time = models.DateTimeField()
    created_at = models.DateTimeField(default=timezone.now)
    is_confirmed = models.BooleanField(default=False)
    is_cancelled = models.BooleanField(default=False)

    def confirm_appointment(self):
        self.is_confirmed = True
        self.save()
    def cancel_appointment(self):
        self.is_cancelled = True
        self.save()
    def is_upcoming_appointment(self):
        if self.appointment_time > timezone.now():
            return True
        else:
            return False
    def __str__(self):
        return f"Appointment with {self.barber} at {self.appointment_time}"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_member = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()

