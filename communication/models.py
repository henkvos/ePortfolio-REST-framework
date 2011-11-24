from django.db import models
from auth.models import TenantModel
from persons.models import Person
from django.utils.translation import ugettext_lazy as _

class Phone(TenantModel):
    TYPE_CHOICES = (
        ('B', _('Business')),
        ('P', _('Private')),
    )
    person = models.ForeignKey(Person, related_name='phones')
    number = models.CharField(max_length=32)
    type = models.CharField(max_length=2, choices=TYPE_CHOICES, blank=True, null=True, default='P')
    is_mobile = models.BooleanField()
    is_default = models.BooleanField()

    def __unicode__(self):
        return self.number
    
class Fax(TenantModel):
    TYPE_CHOICES = (
        ('B', _('Business')),
        ('P', _('Private')),
    )
    person = models.ForeignKey(Person, related_name='faxes')
    number = models.CharField(max_length=32)
    type = models.CharField(max_length=2, choices=TYPE_CHOICES, blank=True, null=True, default='P')
    is_default = models.BooleanField()

    def __unicode__(self):
        return self.number


class Email(TenantModel):
    TYPE_CHOICES = (
        ('B', _('Business')),
        ('P', _('Private')),
    )
    person = models.ForeignKey(Person, related_name='emails')
    address = models.EmailField(max_length=255)
    type = models.CharField(max_length=2, choices=TYPE_CHOICES, blank=True, null=True, default='P')
    is_default = models.BooleanField()

    def __unicode__(self):
        return self.address
