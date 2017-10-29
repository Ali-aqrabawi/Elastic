from django.conf.urls import url
from . import views
from django.http import HttpResponse
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', views.index),
    url(r'^about/', views.about),
    url(r'^analy/', views.analy),
    url(r'^integration/', views.integration),
    url(r'^market/', views.market),
    url(r'^track/', views.track),
    url(r'^careers/', views.careers),
	url(r'^google323523d1a2bbb38c\.html$', lambda r: HttpResponse("google-site-verification: google323523d1a2bbb38c.html", content_type="text/plain")),
	url(r'^sitemap\.xml$', TemplateView.as_view(template_name='sitemap.xml')),
	url(r'^index/', views.index, name='index'),
]