from django.urls import path

from .views import (
    UserListView,
    UserUpdateView,
)

app_name = 'users'

urlpatterns = [
    path('', UserListView.as_view(), name='user-list'),
    path('<str:pk>/update', UserUpdateView.as_view(), name='user-update'),
]