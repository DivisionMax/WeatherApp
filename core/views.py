from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from django.shortcuts import render


# Mixins
class AdminOnlyMixin(UserPassesTestMixin):

    def test_func(self):
        return self.request.user.is_admin


# Views
class AdminUpdateView(LoginRequiredMixin, AdminOnlyMixin, UpdateView):
    pass


class AdminListView(LoginRequiredMixin, AdminOnlyMixin, ListView):
    pass


class AuthListView(LoginRequiredMixin, ListView):
    pass


# Error Handlers
def handler404(request):
    return render(request, '404.html', status=404)


def handler500(request):
    return render(request, '500.html', status=500)


def handler400(request):
    return render(request, '400.html', status=400)


def handler403(request):
    return render(request, '403.html', status=403)
