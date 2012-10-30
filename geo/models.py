from django.db import models
from auth.models import *

from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from utils.fields import UUIDField

class Language(models.Model):
    lcid = models.CharField(primary_key=True, max_length=5)
    en_name = models.CharField(max_length=255)
    loc_name = models.CharField(max_length=255)
    
    def __unicode__(self):
        return u'%s: %s / %s' % (self.lcid, self.en_name, self.loc_name)


class Country(models.Model):
    iso_3166 = models.CharField(primary_key=True, max_length=2)
    iso_3166_1 = models.CharField(max_length=3, null=True, blank=True) #iso_3166-1 is used in leap2a
    en_name = models.CharField(max_length=255)
    loc_name = models.CharField(max_length=255)
    demonym = models.CharField(max_length=255) # = nationaliteit
    default_language = models.ForeignKey(Language)
    citizend_id_name = models.CharField(max_length=255, null=True, blank=True) # e.g. social security number, sofi-nummer, BSN, insurance id etc.
    country_subdivision_name = models.CharField(max_length=255, null=True, blank=True) # e.g. State, Provincie, Departement


    def __unicode__(self):
        return u'%s: %s' % (self.iso_3166, self.en_name)
    
    class Meta:
        verbose_name_plural = 'Countries'
        ordering = ['en_name']


class CountrySubdivision(models.Model):
    iso_3166_2 = models.CharField(primary_key=True, max_length=8)
    name = models.CharField(max_length=255)
    country = models.ForeignKey(Country)
    
    def __unicode__(self):
        return u'%s: %s' % (self.iso_3166_2, self.name)
    
from persons.models import Person
    
class Address(TenantModel):
    TYPE_CHOICES = (
        ('B', _('Business')),
        ('P', _('Private')),
    )
    uuid = UUIDField(auto=True, primary_key=True, db_column='address_id')
    address_line = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=64, null=True, blank=True)
    city = models.CharField(max_length=255)
    country = models.ForeignKey(Country)
    country_subdivision = models.ForeignKey(CountrySubdivision, null=True, blank=True)
    person = models.ForeignKey(Person)
    lat = models.FloatField(null=True, blank=True)
    long = models.FloatField(null=True, blank=True)
    type = models.CharField(max_length=2, choices=TYPE_CHOICES, blank=True, null=True, default='P')
    is_default = models.BooleanField()
    is_correspondence = models.BooleanField()
    is_visit = models.BooleanField()
    
    def __unicode__(self):
        return u'%s %s %s' % (self.address_line, self.zipcode, self.city)
 
    class Meta:
        verbose_name_plural = "Addresses"
    