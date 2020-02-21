import logging

from allauth.account.adapter import DefaultAccountAdapter
from django.conf import settings
from django.http import HttpRequest

logger = logging.getLogger(__name__)


class AccountAdapter(DefaultAccountAdapter):

    def is_open_for_signup(self, request: HttpRequest):
        return getattr(settings, 'ACCOUNT_ALLOW_REGISTRATION')