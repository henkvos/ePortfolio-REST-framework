from django.core.urlresolvers import reverse
from djangorestframework.resources import ModelResource, Resource
from api.resources import ListDetailsResource
from portfolio.models import Portfolio, Education
from persons.models import Person


class PortfolioResource(ListDetailsResource):
    model = Portfolio
    list_fields = ('guid', 
              ('person',('guid', 'full_name',)),
              'status',
              'url',)
    detail_fields = ('guid', 
              #('person',('guid', 'full_name', 'person_details')), 
              'person',
              ('initiator',('username',)),
              'status',
              ('work',('pk' 'job_title')),
              'education',
              ('interests',('pk' 'short_description')),
              ('affiliations',('pk', 'type', 'short_description')),
              )

    def education(self, instance):
        return reverse('Education', kwargs={'portfolio':instance.guid})

    
    def person(self, instance):
        p = Person.objects.get(guid=instance.person.guid)
        pdict = {}
        pdict['guid'] = p.guid
        pdict['full_name'] = p.full_name
        pdict['url'] = reverse('Person', kwargs={'guid':p.guid})
            
        return pdict
    
    
    
    
class EducationResource(ListDetailsResource):
    model = Education
    list_fields = ('pk',
                   'portfolio',
                   'title',
                   'short_description',
                   'url',
                   )
    
    detail_fields = ('pk',
                   'portfolio',
                   'title',
                   'level',
                   'short_description',
                   'description',
                   'start_date',
                   'end_date',
                   'is_current',
                   'is_completed',
                   'is_planned',
                   'organization_name',
                   #'url',
                   )
    def portfolio(self, instance):
        return reverse('Portfolio', kwargs={'guid':instance.portfolio.guid})
   
    
    
    