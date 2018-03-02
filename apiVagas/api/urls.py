from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *


urlpatterns = [
    url(r'^vagas$', VagaList.as_view()),
]
