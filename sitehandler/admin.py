from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(password)
admin.site.register(nameinpersonalinfo)
admin.site.register(emailinpersonalinfo)
admin.site.register(phoneinpersonalinfo)
admin.site.register(addressinpersonalinfo)
admin.site.register(companyinpersonalinfo)
admin.site.register(websiteinpersonalinfo)
admin.site.register(cardsinpayments)
admin.site.register(idcardinids)
admin.site.register(driverlicenseinids)
admin.site.register(extensionuser)
admin.site.register(securenotes)