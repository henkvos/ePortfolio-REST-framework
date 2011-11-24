from django.db import models
from django.contrib.auth.models import User
from auth.models import TenantModel, AuthoringMixin, OnlineIdentityProvider
from geo.models import Country
from utils.fields import UUIDField
import utils.audit as audit
from django.utils.translation import ugettext_lazy as _

def determine_upload_folder(instance, filename):
    return '/'.join([settings.BASE_UPLOAD_FOLDER, str(instance.guid), filename])
    pass

class Person(TenantModel, AuthoringMixin):
    #leap2a spec: 0=not known, 1=male, 2=female, 9=not specified
    GENDER_CHOICES = (
        ('0', _('Unknown')),              
        ('1', _('Male')),
        ('2', _('Female')),
        ('9', _('Not Specified')),
    )
    
    guid = UUIDField(auto=True, primary_key=True)
    legal_family_name = models.CharField(max_length=255)
    legal_given_names = models.CharField(max_length=255, null=True, blank=True)
    preferred_family_name = models.CharField(max_length=255, null=True, blank=True)
    preferred_given_name = models.CharField(max_length=255, null=True, blank=True)
    middle_name = models.CharField(max_length=255, null=True, blank=True)
    initials = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    prefix = models.CharField(max_length=255, null=True, blank=True)
    suffix = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, blank=True, null=True, default='9')
    date_of_birth = models.DateField(blank=True, null=True)
    place_of_birth = models.CharField(max_length=255, blank=True, null=True)
    country_of_birth = models.ForeignKey(Country, null=True, blank=True, related_name="country_of_birth")
    country_of_origin = models.ForeignKey(Country, null=True, blank=True, related_name="country_of_origin") #used in NEN NTA 2035: land van herkomst ivm immigratie
    profile_picture = models.ImageField(blank=True, null=True, upload_to=determine_upload_folder)
    marital_status = models.CharField(max_length=255, blank=True, null=True)
    
    history = audit.AuditTrail(show_in_admin=True)

    def __unicode__(self):
        return u'%s, %s %s' % (self.legal_family_name, self.preferred_given_name, self.middle_name)
    
    def full_legal_name(self):
        return self.legal_given_names + ( (' ' + self.middle_name) if self.middle_name else '') + ' ' + self.legal_family_name
    
    def full_name(self):
        return self.preferred_given_name + ( (' ' + self.middle_name) if self.middle_name else '') + ' ' + self.legal_family_name
    

    def name_inverted(self):
        return self.legal_family_name + ', ' + self.preferred_given_name + ( (' ' + self.middle_name) if self.middle_name else '')
    
    class Meta:
        verbose_name_plural = "Persons"
        #ordering = ['legal_family_name', 'preferred_given_name']
        

class OnlineIdentity(TenantModel):
    provider = models.ForeignKey(OnlineIdentityProvider)
    user = models.ForeignKey(User, null=True, blank=True)
    person = models.ForeignKey(Person, null=True, blank=True)
    identifier = models.URLField(verify_exists=False, max_length=255)
    access_tokens = models.TextField(blank=True, null=True)
    page_url = models.URLField(blank=True, verify_exists=False)
    profile_pic_url = models.URLField(blank=True, verify_exists=False)
    
    def __unicode__(self):
        return u'%s ( %s )' % (self.user.name, self.provider.name)
    
    class Meta:
        verbose_name_plural = "Online Identities"
        


