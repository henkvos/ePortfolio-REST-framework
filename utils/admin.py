from django.contrib import admin
from auth.models import *
from persons.models import *
from geo.models import *
from legal.models import *
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

#indentity
class CitizenshipInline(admin.TabularInline):
    model = Citizenship
    extra = 1
    fields = ('country', 'citizen_id', 'passport_number')

class PersonAdmin(admin.ModelAdmin):
    model = Person
    inlines = [
        CitizenshipInline,
    ]
    #fields = ('last_name', 'first_name', 'middle_name')
    
class RepresentativeAdmin(admin.ModelAdmin):
    model = Representative
    


admin.site.register(Session, SessionAdmin)   

admin.site.register(Tenant, TenantAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(OnlineIdentityProvider, OnlineIdentityProviderAdmin)
admin.site.register(OnlineIdentity, OnlineIdentityAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Representative, RepresentativeAdmin)

