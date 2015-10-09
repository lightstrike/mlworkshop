from django.conf.urls import patterns, url
from . import views


urlpatterns = patterns('reports.views',
	url(r'^$', views.results_list, name='results_list'),
	url(r'^query/$', views.query_view, name='query'),
	url(r'^results/(?P<pk>[0-9]+)/$', views.results_detail, name='results_detail'),
)

