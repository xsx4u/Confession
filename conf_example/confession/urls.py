from django.conf.urls import patterns, url

from confession import views
from confession.views import SubmitView, AboutView, MessageView, DetailView, SuccessView

urlpatterns = patterns('',
	url(r'^$', views.index_view, name='index'),
	url(r'confession/(?P<confession_id>\d+)/$', DetailView.as_view(), name='detail'),
	url(r'^submit', SubmitView.as_view(), name='submit'),
	url(r'^about', AboutView.as_view(), name="about"),
	url(r'^message', MessageView.as_view(), name='message'),
	url(r'^success', SuccessView.as_view(), name='success'),
	)

# This is needed to serve static files like images and css
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()