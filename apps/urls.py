from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()

from apps import views
from TestCaser import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',views.index),
    url(r'^index/$',views.index),
]
