from django.conf.urls.defaults import patterns, include, url

from djangorestframework.resources import ModelResource
from djangorestframework.views import ListOrCreateModelView, InstanceModelView
from api.views import ListView, DetailView, ListOrCreateView

from portfolio.resources import PortfolioResource, EducationResource
from portfolio.views import PortfolioView, EducationView

from persons.resources import PersonResource



urlpatterns = patterns('',
    #url(r'^$', ListOrCreateView.as_view(resource=PortfolioResource)),
    url(r'^portfolios/$', ListOrCreateView.as_view(resource=PortfolioResource), name='Portfolios'),
    url(r'^portfolio/(?P<guid>[^/]+)/$', DetailView.as_view(resource=PortfolioResource), name='Portfolio'),
    url(r'^portfolios/(?P<person>[^/]+)/$', ListOrCreateView.as_view(resource=PortfolioResource), name='Portfolios-Person'),
    url(r'^portfolio/(?P<portfolio>[^/]+)/education/$', ListOrCreateView.as_view(resource=EducationResource), name='Education'),
    url(r'^portfolio/(?P<portfolio>[^/]+)/education/(?P<pk>[^/]+)/$', DetailView.as_view(resource=EducationResource), name='Education-Detail'),
    #url(r'^(?P<portfolio>[^/]+)/education/$', ListOrCreateView.as_view(resource=EducationResource), name='Education'),
    #url(r'^portfolios/(?P<guid>[^/]+)/educations/(?P<pk>[^/]+)/$', DetailView.as_view(resource=EducationResource), name='Education'),
    #url(r'^educations/$', ListOrCreateView.as_view(resource=EducationResource), name='Educations'),
    #url(r'^educations/(?P<pk>[^/]+)/$', DetailView.as_view(resource=EducationResource), name='Education'),
    #url(r'^/kenniscentra$', ListView.as_view(resource=KenniscentrumResource), name='Kenniscentra'),
    url(r'^persons/$', ListOrCreateView.as_view(resource=PersonResource), name='Persons'),
    url(r'^person/(?P<guid>[^/]+)/$', DetailView.as_view(resource=PersonResource), name='Person'),
    
)