from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User
from django.conf import settings
import utils.audit as audit
from django.utils.translation import ugettext_lazy as _

MULTI_TENANT = settings.MULTI_TENANT

class TenantManager(models.Manager):
    def for_tenant(self, tenant):
        if tenant_id:
            return super(TenantManager, self).get_query_set().filter(Q(tenant=tenant)|Q(tenant=0))
        else:
            return super(TenantManager, self).get_query_set().all()
        
class PublicManager(models.Manager):
    def for_tenant(self, tenant):
        return super(PublicManager, self).get_query_set().all()
        

        
class Tenant(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    login_url = models.CharField(max_length=255, blank=True, null=True)
    theme_css_url = models.URLField(max_length=255, blank=True, null=True)
    allow_cross_tenant_sharing = models.BooleanField(default=False)
    
    def __unicode__(self):
        return u'%s ( %s )' % (self.name, self.id)
    
    class Meta:
        ordering = ['name']
        
class AuthoringMixin(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)
    created_by = models.ForeignKey(User, blank=True, null=True, related_name="created_by")
    last_modified = models.DateTimeField(auto_now=True, auto_now_add=True, editable=False)
    last_modified_by = models.ForeignKey(User, blank=True, null=True, related_name="last_modified_by")


class TenantModel(models.Model):
    tenant = models.ForeignKey(Tenant, default=0, blank=True, null=True)
    
    if MULTI_TENANT:
        objects = TenantManager() # The multi-tenant manager.
    else:
        objects = models.Manager() # The default manager.
        
    class Meta:
        abstract = True
        
        
class OnlineIdentityProvider(models.Model):
    name = models.CharField(max_length=255)
    is_social_media = models.BooleanField(default=True)
    is_oauth_provider = models.BooleanField(default=True)
    oauth_consumer_key = models.CharField(max_length=255, null=True, blank=True)
    oauth_consumer_secret_key = models.CharField(max_length=255, null=True, blank=True)
    
    def __unicode__(self):
        return u'%s ( %s )' % (self.name, self.id)








