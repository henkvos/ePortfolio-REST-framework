from django.core.urlresolvers import reverse
from djangorestframework.resources import ModelResource, Resource
from api.resources import ListDetailsResource
from portfolio.models import Portfolio, Education
from persons.models import Person

class PersonResource(ListDetailsResource):
    model = Person
    list_fields = ('guid', 
                   'url',
                   'full_name'
                   )
    detail_fields = ('guid',
                     #'tenant',
                     'legal_family_name',
                     'legal_given_names',
                     'gender',
                     'marital_status',
                     #'url',
                     'portfolios',
                     #('country_of_birth',('__unicode__',)),
                     
                     )
    
    def portfolios(self, instance):
        ports = Portfolio.objects.filter(person=instance.guid)
        portlist = []
        for port in ports:
            portdict = {}
            portdict['guid'] = port.guid
            portdict['url'] = reverse('Portfolio', kwargs={'guid':port.guid})
            portlist.append(portdict)
            
        return portlist

