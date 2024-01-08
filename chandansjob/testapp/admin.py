from django.contrib import admin
from testapp.models import Hydjobs
from testapp.models import Punejobs
from testapp.models import Bangjobs


# Register your models here.
class HydjobAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','address','email','phonenumber']

admin.site.register(Hydjobs,HydjobAdmin)

class PunejobAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','address','email','phonenumber']

admin.site.register(Punejobs,PunejobAdmin)

class BangjobAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','address','email','phonenumber']

admin.site.register(Bangjobs,BangjobAdmin)
