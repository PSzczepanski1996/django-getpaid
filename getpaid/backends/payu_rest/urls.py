from django.conf.urls import url

from .views import ConfirmationWebhook


urlpatterns = [
    url(r'^confirm/$', csrf_exempt(ConfirmationWebhook.as_view()), name='confirm'),
]
