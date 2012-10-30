from django.core.urlresolvers import reverse
from djangorestframework.resources import ModelResource, Resource
from api.resources import ListDetailsResource
from portfolio.models import Portfolio, Education, Work, Interest, Affiliation, Product, Artefact
from persons.models import Person



class PortfolioResource(ListDetailsResource):
    model = Portfolio
    list_fields = ('uuid', 
                   'person',
              'status',
              'url',)
    detail_fields = ('uuid',
              'person',
              ('initiator',('username','id')),
              'status',
              'work',
              'education',
              'interests',
              'affiliations'
              )
    
    def education(self, instance):
        qlist = Education.objects.filter(portfolio=instance.uuid)
        rlist = []
        for item in qlist:
            rdict = {}
            rdict['uuid'] = item.uuid
            rdict['url'] = reverse('Education-Detail', kwargs={'portfolio':instance.uuid, 'uuid':item.uuid})
            rdict['title'] = item.title
            rlist.append(rdict)

        return rlist
    
    def work(self, instance):
        qlist = Work.objects.filter(portfolio=instance.uuid)
        rlist = []
        for item in qlist:
            rdict = {}
            rdict['uuid'] = item.uuid
            rdict['url'] = reverse('Work-Detail', kwargs={'portfolio':instance.uuid, 'uuid':item.uuid})
            rdict['title'] = item.title
            rlist.append(rdict)

        return rlist
    
    
    def person(self, instance):
        p = Person.objects.get(uuid=instance.person.uuid)
        pdict = {}
        pdict['uuid'] = p.uuid
        pdict['full_name'] = p.full_name
        pdict['url'] = reverse('Person', kwargs={'uuid':p.uuid})
            
        return pdict
    

    def interests(self, instance):
        qlist = Interest.objects.filter(portfolio=instance.uuid)
        rlist = []
        for item in qlist:
            rdict = {}
            rdict['uuid'] = item.uuid
            rdict['url'] = reverse('Interest-Detail', kwargs={'portfolio':instance.uuid, 'uuid':item.uuid})
            rdict['title'] = item.title
            rlist.append(rdict)

        return rlist
    
    def affiliations(self, instance):
        qlist = Affiliation.objects.filter(portfolio=instance.uuid)
        rlist = []
        for item in qlist:
            rdict = {}
            rdict['uuid'] = item.uuid
            rdict['url'] = reverse('Affiliation-Detail', kwargs={'portfolio':instance.uuid, 'uuid':item.uuid})
            rdict['title'] = item.title
            rlist.append(rdict)

        return rlist

    
    
    
'''
    ports = Portfolio.objects.filter(person=instance.guid)
        portlist = []
        for port in ports:
            portdict = {}
            portdict['guid'] = port.guid
            portdict['url'] = reverse('Portfolio', kwargs={'guid':port.guid})
            portlist.append(portdict)
            
        return portlist
'''
   
    
    
    
class EducationResource(ListDetailsResource):
    model = Education
    list_fields = ('uuid',
                   'portfolio',
                   'title',
                   'short_description',
                   'url'
                   )
    
    detail_fields = ('uuid',
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
                   'organization_name'
                   )
    
    def portfolio(self, instance):
        pdict = {}
        pdict['uuid'] = instance.portfolio.uuid
        pdict['full_name'] = instance.portfolio.person.full_name
        pdict['url'] = reverse('Portfolio-Detail', kwargs={'uuid':instance.portfolio.uuid})
        
        return pdict
    
    
class WorkResource(ListDetailsResource):
    model = Work
    list_fields = ('uuid',
                   'portfolio',
                   'title',
                   'short_description',
                   'url'
                   )
    
    detail_fields = ('uuid',
                   'portfolio',
                   'title',
                   'function',
                   'short_description',
                   'description',
                   'start_date',
                   'end_date',
                   'is_current',
                   'is_completed',
                   'is_planned',
                   'organization_name'
                   )
    
    def portfolio(self, instance):
        pdict = {}
        pdict['uuid'] = instance.portfolio.uuid
        pdict['full_name'] = instance.portfolio.person.full_name
        pdict['url'] = reverse('Portfolio-Detail', kwargs={'uuid':instance.portfolio.uuid})
        
        return pdict
    
class InterestResource(ListDetailsResource):
    model = Interest
    list_fields = ('uuid',
                   'portfolio',
                   'title',
                   'short_description',
                   'url'
                   )
    
    detail_fields = ('uuid',
                   'portfolio',
                   'title',
                   'level',
                   'status',
                   'short_description',
                   'description',
                   'start_date',
                   'end_date',
                   'is_current',
                   'is_completed',
                   'is_planned',
                   'organization_name'
                   )
    
    def portfolio(self, instance):
        pdict = {}
        pdict['uuid'] = instance.portfolio.uuid
        pdict['full_name'] = instance.portfolio.person.full_name
        pdict['url'] = reverse('Portfolio-Detail', kwargs={'uuid':instance.portfolio.uuid})
        
        return pdict
    
class AffiliationResource(ListDetailsResource):
    model = Affiliation
    list_fields = ('uuid',
                   'portfolio',
                   'title',
                   'short_description',
                   'url'
                   )
    
    detail_fields = ('uuid',
                   'portfolio',
                   'title',
                   'type',
                   'role',
                   'short_description',
                   'description',
                   'start_date',
                   'end_date',
                   'is_current',
                   'is_completed',
                   'is_planned',
                   'organization_name'
                   )
    
    def portfolio(self, instance):
        pdict = {}
        pdict['uuid'] = instance.portfolio.uuid
        pdict['full_name'] = instance.portfolio.person.full_name
        pdict['url'] = reverse('Portfolio-Detail', kwargs={'uuid':instance.portfolio.uuid})
        
        return pdict
    

    