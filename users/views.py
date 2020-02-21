from django.urls import reverse

from .models import WeatherAppUser

from core.views import AdminListView, AdminUpdateView


class UserListView(AdminListView):

    model = WeatherAppUser
    paginate_by = 3
    template_name = 'users/user_list.html'

    context_object_name = 'users'


class UserUpdateView(AdminUpdateView):
    model = WeatherAppUser
    template_name = 'users/user_update.html'

    fields = ['email', 'first_name', 'last_name']

    def get_success_url(self):
        return reverse('users:user-list')
