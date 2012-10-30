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
    pass

class EducationDetailView(DetailView):
    pass


