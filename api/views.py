from django.core.urlresolvers import reverse

from djangorestframework.views import View, ListModelView, InstanceModelView,  ListOrCreateModelView
from djangorestframework.mixins import *
from djangorestframework.utils import as_tuple

class ListView(ListModelView):
    allowed_methods = ('GET',)


class ListOrCreateView(ListOrCreateModelView):
    allowed_methods = ('GET', 'POST')


class DetailView(InstanceModelView):
    allowed_methods = ('GET', 'PUT', 'DELETE')


class ListQuickSearchView(ListModelView):
    allowed_methods = ('GET',)
    queryset = None

    def get(self, request, *args, **kwargs):
        term = request.GET.get('term', '')
        model = self.resource.model
        queryset = self.queryset if self.queryset is not None else model.objects.all()

        if hasattr(self, 'resource'):
            ordering = getattr(self.resource, 'ordering', None)
        else:
            ordering = None

        if ordering:
            args = as_tuple(ordering)
            queryset = queryset.order_by(*args)
        return queryset.filter(title__startswith=term)
    

class ListSearchView(ListModelView):
    allowed_methods = ('GET',)
    queryset = None

    def get(self, request, *args, **kwargs):
        term = request.GET.get('term', '')
        model = self.resource.model
        queryset = self.queryset if self.queryset is not None else model.objects.all()

        if hasattr(self, 'resource'):
            ordering = getattr(self.resource, 'ordering', None)
        else:
            ordering = None

        if ordering:
            args = as_tuple(ordering)
            queryset = queryset.order_by(*args)
        return queryset.filter(title__contains=term)
    
