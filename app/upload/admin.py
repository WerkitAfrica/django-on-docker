from django.contrib import admin

# Register your models here.
from upload.models import Invoice, Company, Person, Email, Payment

admin.site.register(Invoice)
admin.site.register(Company)
admin.site.register(Person)
admin.site.register(Email)
admin.site.register(Payment)