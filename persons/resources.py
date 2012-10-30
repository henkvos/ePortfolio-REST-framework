from django.core.urlresolvers import reverse
from djangorestframework.resources import ModelResource, Resource
from api.resources import ListDetailsResource
from portfolio.models import Portfolio, Education
from persons.models import Person

class PersonResource(ListDetailsResource):
    model = Person
    list_fields = ('uuid', 
                   'url',
                   'full_name'
                   )
    detail_fields = ('uuid',
                     #'tenant',
                     'legal_family_name',
                     'legal_given_names',
                     'gender',
                     'marital_status',
                     'portfolios',
                     #('country_of_birth',('__unicode__',)),
                     
                     )
    
    def portfolios(self, instance):
        ports = Portfolio.objects.filter(person=instance.uuid)
        portlist = []
        for port in ports:
            portdict = {}
            portdict['uuid'] = port.uuid
            portdict['url'] = reverse('Portfolio-Detail', kwargs={'uuid':port.uuid})
            portlist.append(portdict)
            
        return portlist

