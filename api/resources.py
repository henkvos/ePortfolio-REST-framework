from django.core.urlresolvers import reverse
from djangorestframework.resources import ModelResource, Resource
#from evc.models import KBB, Competence, Component, Vaardigheid, Dossier, Kerntaak, Werkproces, Uitstroom, Uitstroom_Kerntaak, Uitstroom_Werkproces, Uitstroom_Competentie, Uitstroom_Component, Uitstroom_Vaardigheid
from api.views import ListView, ListOrCreateView, DetailView, ListSearchView, ListQuickSearchView

class ListDetailsResource(ModelResource):
    def __init__(self, view):

        super(ModelResource, self).__init__(view)

        self.model = getattr(view, 'model', None) or self.model
        
        if self.view.__class__ == ListView:
            self.fields = getattr(self, 'list_fields', None) or self.fields
        elif self.view.__class__ == ListOrCreateView:
            self.fields = getattr(self, 'list_fields', None) or self.fields
        elif self.view.__class__ == ListSearchView:
            self.fields = getattr(self, 'search_fields', None) or self.fields
        elif self.view.__class__ == ListQuickSearchView:
            self.fields = getattr(self, 'search_fields', None) or self.fields
        elif self.view.__class__ == DetailView:
            self.fields = getattr(self, 'detail_fields', None) or self.fields
        else:
            self.fields = self.fields
            
