from django.contrib.auth.models import AbstractUser


class WeatherAppUser(AbstractUser):
    """
    Override base user for easier long-term options
    """
    def __str__(self):
        return self.email

    @property
    def is_admin(self):
        return self.is_staff or self.is_superuser
