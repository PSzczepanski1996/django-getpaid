from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from .views import ConfirmationWebhook


urlpatterns = [
    url(r'^confirm/$', csrf_exempt(ConfirmationWebhook.as_view()), name='confirm'),
]
