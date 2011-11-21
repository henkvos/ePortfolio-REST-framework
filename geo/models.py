from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

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