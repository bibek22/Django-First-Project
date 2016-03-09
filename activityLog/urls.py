from django.conf.urls import url
from . import views

urlpatterns = [
    # the base.
    url(r'^$', views.default),
    url(r'^(?P<sn>[0-9]+)/edit', views.add_entry, name='edit'),
    url(r'^add$', views.add, name='add'),
    url(r'^(?P<id>[0-9]+)/del/', views.default, name="del"),
]
