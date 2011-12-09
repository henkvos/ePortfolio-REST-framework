from django.conf.urls.defaults import patterns, include, url

from djangorestframework.resources import ModelResource
from djangorestframework.views import ListOrCreateModelView, InstanceModelView
from api.views import ListView, DetailView, ListOrCreateView

from portfolio.resources import PortfolioResource, EducationResource, WorkResource, InterestResource, AffiliationResource
from portfolio.views import PortfolioView, EducationView

from persons.resources import PersonResource



urlpatterns = patterns('',
    #url(r'^$', ListOrCreateView.as_view(resource=PortfolioResource)),
    url(r'^portfolios/$', ListOrCreateView.as_view(resource=PortfolioResource), name='Portfolio-List'),
    url(r'^portfolios/(?P<uuid>[^/]+)/$', DetailView.as_view(resource=PortfolioResource), name='Portfolio-Detail'),
    url(r'^portfolios/(?P<person>[^/]+)/$', ListOrCreateView.as_view(resource=PortfolioResource), name='Portfolios-Person'),
    url(r'^education/$', ListOrCreateView.as_view(resource=EducationResource), name='Education'),
    url(r'^portfolios/(?P<portfolio>[^/]+)/education/$', ListOrCreateView.as_view(resource=EducationResource), name='Education-List'),
    url(r'^portfolios/(?P<portfolio>[^/]+)/education/(?P<uuid>[^/]+)/$', DetailView.as_view(resource=EducationResource), name='Education-Detail'),
    url(r'^work/$', ListOrCreateView.as_view(resource=WorkResource), name='Work'),
    url(r'^portfolios/(?P<portfolio>[^/]+)/work/$', ListOrCreateView.as_view(resource=WorkResource), name='Work-List'),
    url(r'^portfolios/(?P<portfolio>[^/]+)/work/(?P<uuid>[^/]+)/$', DetailView.as_view(resource=WorkResource), name='Work-Detail'),
    url(r'^interests/$', ListOrCreateView.as_view(resource=InterestResource), name='Interests'),
    url(r'^portfolios/(?P<portfolio>[^/]+)/interests/$', ListOrCreateView.as_view(resource=InterestResource), name='Interest-List'),
    url(r'^portfolios/(?P<portfolio>[^/]+)/interest/(?P<uuid>[^/]+)/$', DetailView.as_view(resource=InterestResource), name='Interest-Detail'),
    url(r'^affiliations/$', ListOrCreateView.as_view(resource=AffiliationResource), name='Affiliations'),
    url(r'^portfolios/(?P<portfolio>[^/]+)/affiliations/$', ListOrCreateView.as_view(resource=AffiliationResource), name='Affiliation-List'),
    url(r'^portfolios/(?P<portfolio>[^/]+)/affiliation/(?P<uuid>[^/]+)/$', DetailView.as_view(resource=AffiliationResource), name='Affiliation-Detail'),
    url(r'^persons/$', ListOrCreateView.as_view(resource=PersonResource), name='Persons'),
    url(r'^persons/(?P<uuid>[^/]+)/$', DetailView.as_view(resource=PersonResource), name='Person'),  
)