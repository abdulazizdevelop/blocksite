from django.contrib import admin
from .models import Banner ,Contact , About ,Service, Testimonial, ContactPersonal

# Register your models here.

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    pass


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display =['id','name','email'  ]


class Aboutadmin(admin.ModelAdmin):
    list_display = ['id' , 'title']
    search_fields = ('id', 'title', 'description')
     
admin.site.register(About, Aboutadmin)
admin.site.register(Testimonial)
admin.site.register(ContactPersonal)
admin.site.register(Service)