from django.test import TestCase
from ..models import WeatherAppUser


class UserTests(TestCase):
    def setUp(self):
        self.user_regular = WeatherAppUser.objects.create_user(
            "regular",
            email="test@gmail.com",
            password="random password",
        )
        self.user_superuser = WeatherAppUser.objects.create_user(
            "superuser",
            email="super@gmail.com",
            password="random password",
            is_superuser=True,
        )
        self.user_staff = WeatherAppUser.objects.create_user(
            "staff",
            email="staff@gmail.com",
            password="random password",
            is_staff=True,
        )

    def test_user_admin_property(self):

        self.assertEquals(self.user_regular.is_admin, False)
        self.assertEquals(self.user_superuser.is_admin, True)
        self.assertEquals(self.user_staff.is_admin, True)
