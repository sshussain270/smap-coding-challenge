from django.conf.urls import url
from . import views

#Add your urls here
urlpatterns = [
    url(r'^$', views.summary),
    url(r'^summary/', views.summary, name="Summary"),
    url(r'^detail/(?P<pk>[0-9]+)/$', views.detail, name="detail"),
]
