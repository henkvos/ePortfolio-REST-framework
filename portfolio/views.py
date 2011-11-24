from django.core.urlresolvers import reverse
from portfolio.models import Portfolio, Education
from persons.models import Person


from djangorestframework.views import View, ListModelView, InstanceModelView
from djangorestframework.mixins import *
from djangorestframework.utils import as_tuple
from api.views import ListView, DetailView, ListOrCreateView
from portfolio.resources import PortfolioResource, EducationResource


class PortfolioView(ListOrCreateView):
    pass

class PortfolioDetailView(DetailView):
    pass

class EducationView(ListOrCreateView):
    
    def get(self, request, *args, **kwargs):
        model = self.resource.model
        print kwargs
        pk = kwargs['guid']
        portfolio = Portfolio.objects.get(pk=pk)
        education = model.objects.filter(portfolio=portfolio)

        return education
    
    
        


class EducationDetailView(DetailView):
    pass


