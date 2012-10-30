from django.contrib import admin
from auth.models import *
from persons.models import *
from geo.models import *
from legal.models import *
from communication.models import *
from portfolio.models import *
from django.contrib.sessions.models import Session


#session info
class SessionAdmin(admin.ModelAdmin):
    def _session_data(self, obj):
        return obj.get_decoded()
    list_display = ['session_key', '_session_data', 'expire_date']
    

#auth info    
class TenantAdmin(admin.ModelAdmin):
    model = Tenant
    
class OnlineIdentityProviderAdmin(admin.ModelAdmin):
    model = OnlineIdentityProvider
    
class OnlineIdentityAdmin(admin.ModelAdmin):
    model = OnlineIdentity
    
class UserProfileAdmin(admin.ModelAdmin):
    model = UserProfile
    
#geographic

class LanguageAdmin(admin.ModelAdmin):
    model = Language

class CountrySubdivisionInline(admin.TabularInline):
    model = CountrySubdivision
    extra = 1
    #fields = ('country', 'name', 'iso_3166_2')

class CountryAdmin(admin.ModelAdmin):
    model = Country
    inlines = [
        CountrySubdivisionInline,
    ]
    
class AddressAdmin(admin.ModelAdmin):
    model = Address

    
#communication

class EmailAdmin(admin.ModelAdmin):
    model = Email

    
class PhoneAdmin(admin.ModelAdmin):
    model = Phone

    
class FaxAdmin(admin.ModelAdmin):
    model = Fax


#identity
class CitizenshipInline(admin.ModelAdmin):
    model = Citizenship
    

class PersonAdmin(admin.ModelAdmin):
    model = Person
   
    #fields = ('last_name', 'first_name', 'middle_name')
    
class RepresentationAdmin(admin.ModelAdmin):
    model = Representation
    
    
class EducationAdmin(admin.ModelAdmin):
    model = Education
    

class WorkAdmin(admin.ModelAdmin):
    model = Work


class InterestAdmin(admin.ModelAdmin):
    model = Interest

    
class AffiliationAdmin(admin.ModelAdmin):
    model = Affiliation

    
class PortfolioAdmin(admin.ModelAdmin):
    model = Portfolio

    
class ArtefactAdmin(admin.ModelAdmin):
    model = Artefact

    
class ProductAdmin(admin.ModelAdmin):
    model = Product


admin.site.register(Session, SessionAdmin)   

admin.site.register(Tenant, TenantAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(OnlineIdentityProvider, OnlineIdentityProviderAdmin)
admin.site.register(OnlineIdentity, OnlineIdentityAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Phone, PhoneAdmin)
admin.site.register(Email, EmailAdmin)
admin.site.register(Fax, FaxAdmin)
admin.site.register(Representation, RepresentationAdmin)
admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Work, WorkAdmin)
admin.site.register(Interest, InterestAdmin)
admin.site.register(Affiliation, AffiliationAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Artefact, ArtefactAdmin)


