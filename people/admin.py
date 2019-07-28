from django.contrib import admin
from .models import People

# Register your models here.


class PeopleAdmin(admin.ModelAdmin):
    list_display = ("First_Name", "Last_Name", "Address", "DateO_of_Birth")


admin.site.register(People, PeopleAdmin)
