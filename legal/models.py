from django.db import models
from auth.models import TenantModel, AuthoringMixin
from geo.models import Country
from persons.models import Person
from utils.fields import UUIDField
import utils.audit as audit
from django.utils.translation import ugettext_lazy as _

class Representative(TenantModel):
    TYPE_CHOICES = (   
        ('1', _('Parent')),
        ('2', _('Guardian')),
        ('3', _('Curator')),
        ('4', _('Plenipotentiary')),
    )
    type = models.CharField(max_length=2, choices=TYPE_CHOICES, default='1')
    representant = models.ForeignKey(Person, related_name="representant")
    represents = models.ForeignKey(Person)

    def __unicode__(self):
        return u'%s (%s): %s' % (self.representant.name_inverted, self.type, self.represents.name_inverted)
        
        
class Citizenship(TenantModel):
    citizen_id = models.CharField(max_length=255)
    person = models.ForeignKey(Person)
    passport_number= models.CharField(max_length=255, null=True, blank=True)
    country =  models.ForeignKey(Country)
    
    def __unicode__(self):
        return u'%s: %s' % (self.citizen_id, self.person.name_inverted)
    
