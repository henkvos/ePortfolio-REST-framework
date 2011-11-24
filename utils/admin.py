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
    
class AddressInline(admin.StackedInline):
    model = Address
    extra = 0
    
#communication

class EmailInline(admin.TabularInline):
    model = Email
    extra = 0
    
class PhoneInline(admin.TabularInline):
    model = Phone
    extra = 0
    
class FaxInline(admin.TabularInline):
    model = Fax
    extra = 0
    
    

#identity
class CitizenshipInline(admin.TabularInline):
    model = Citizenship
    extra = 0
    fields = ('country', 'citizen_id', 'passport_number')

class PersonAdmin(admin.ModelAdmin):
    model = Person
    inlines = [
        AddressInline,
        EmailInline,
        PhoneInline,
        FaxInline,       
        CitizenshipInline,
    ]
    #fields = ('last_name', 'first_name', 'middle_name')
    
class RepresentativeAdmin(admin.ModelAdmin):
    model = Representative
    
    
class EducationInline(admin.StackedInline):
    model = Education
    extra = 0
    
class WorkInline(admin.StackedInline):
    model = Work
    extra = 0
    
class InterestInline(admin.StackedInline):
    model = Interest
    extra = 0
    
class AffiliationInline(admin.StackedInline):
    model = Affiliation
    extra = 0
    
class PortfolioAdmin(admin.ModelAdmin):
    model = Portfolio
    inlines = [
        EducationInline,
        WorkInline,
        InterestInline,
        AffiliationInline
    ]
    
class ArtefactInline(admin.StackedInline):
    model = Artefact
    extra = 0
    
class ProductAdmin(admin.ModelAdmin):
    model = Product
    inlines = [
        ArtefactInline,
    ]


admin.site.register(Session, SessionAdmin)   

admin.site.register(Tenant, TenantAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(OnlineIdentityProvider, OnlineIdentityProviderAdmin)
admin.site.register(OnlineIdentity, OnlineIdentityAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Representative, RepresentativeAdmin)
admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Product, ProductAdmin)


