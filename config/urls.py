from django.conf.urls import include, url
from django.contrib import admin

from chronic_medicare import urls as chronic_urls


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^chronic-medicare/', include(chronic_urls, namespace="chronic"))
]
