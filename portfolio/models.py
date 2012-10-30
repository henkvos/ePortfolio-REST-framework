from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from auth.models import TenantModel, AuthoringMixin
from persons.models import Person
from utils.fields import UUIDField
import utils.audit as audit
from django.utils.translation import ugettext_lazy as _

class Portfolio(TenantModel, AuthoringMixin):
    STATUS_CHOICES = (
        ('0', _('Not Active')),
        ('1', _('Active')),
    )
    uuid = UUIDField(auto=True, primary_key=True, db_column='portfolio_id')
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, blank=True, null=True, default='1')
    person = models.ForeignKey(Person, related_name="portfolios")
    initiator = models.ForeignKey(User)
    
    #history = audit.AuditTrail(show_in_admin=True)
    
    def __unicode__(self):
        return u'%s: %s' % (self.uuid, self.person.full_name())

    
class Activity(TenantModel):
    short_description = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    is_current = models.NullBooleanField(default=False, null=True, blank=True)
    is_completed = models.NullBooleanField(default=True, null=True, blank=True)
    is_planned = models.NullBooleanField(default=False, null=True, blank=True)
    organization_name = models.CharField(max_length=255, null=True, blank=True)
    
    def __unicode__(self):
        return u'%s (%s)' % (self.short_description, self.portfolio.uuid)
    
    class Meta:
        abstract = True
        
    
class Education(Activity):
    uuid = UUIDField(auto=True, primary_key=True, db_column='education_id')
    portfolio = models.ForeignKey(Portfolio, related_name="education")
    title = models.CharField(max_length=255)
    level = models.CharField(max_length=255, null=True, blank=True)
    
    def __unicode__(self):
        return u'%s (%s)' % (self.title, self.portfolio.uuid)
    
    class Meta:
        verbose_name_plural = 'Education'
 

class Affiliation(Activity):
    uuid = UUIDField(auto=True, primary_key=True, db_column='affiliation_id')
    portfolio = models.ForeignKey(Portfolio, related_name="affiliations")
    type = models.CharField(max_length=64)
    title = models.CharField(max_length=255)
    role = models.CharField(max_length=255, blank=True, null=True)
    
    def __unicode__(self):
        return u'%s (%s)' % (self.type, self.portfolio.uuid)
     
    
class Work(Activity):
    uuid = UUIDField(auto=True, primary_key=True, db_column='work_id')
    portfolio = models.ForeignKey(Portfolio, related_name="work")
    title = models.CharField(max_length=255)
    function = models.CharField(max_length=255, null=True, blank=True)
    
    def __unicode__(self):
        return u'%s (%s)' % (self.title, self.portfolio.uuid)
    
    class Meta:
        verbose_name_plural = 'Work'
    
    
class Interest(Activity):
    STATUS_CHOICES = (
        ('0', _('Not Active')),
        ('1', _('Active')),
    )
    uuid = UUIDField(auto=True, primary_key=True, db_column='interest_id')
    portfolio = models.ForeignKey(Portfolio, related_name="interests")
    title = models.CharField(max_length=255)
    level = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, blank=True, null=True, default='1')
    
    def __unicode__(self):
        return u'%s (%s)' % (self.short_description, self.status)
  

class Product(TenantModel):
    TYPE_CHOICES = (
        ('cert', _('Certificate')),
        ('dipl', _('Diploma')),
        ('pict', _('Picture')),
        ('recl', _('Letter of recommendation')),
    )
    uuid = UUIDField(auto=True, primary_key=True, db_column='product_id')
    portfolio = models.ForeignKey(Portfolio, related_name="products")
    education = models.ForeignKey(Education, blank=True, null=True)
    work = models.ForeignKey(Work, blank=True, null=True)
    interest = models.ForeignKey(Interest, blank=True, null=True)
    affiliation = models.ForeignKey(Affiliation, blank=True, null=True)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=4, choices=TYPE_CHOICES, blank=True, null=True)
    date = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    
    def __unicode__(self):
        return u'%s (%s)' % (self.name, self.type)


def determine_upload_folder(instance, filename):
    return '/'.join([settings.BASE_UPLOAD_FOLDER, str(instance.product.portfolio.uuid), str(instance.product), filename])
    pass

class Artefact(TenantModel):
    uuid = UUIDField(auto=True, primary_key=True, db_column='artefact_id')
    attachment = models.FileField(upload_to=determine_upload_folder)
    product = models.ForeignKey(Product)
    mimetype = models.CharField(max_length=255, editable=False)
    size = models.IntegerField(null=True, blank=True)
    
    def __unicode__(self):
        return self.attachment.name
    
    def filename(self):
        return os.path.basename(self.attachment.name)
        
