# coding: utf-8

from django.contrib import admin

# Register your models here.

from django.contrib import admin
from eventex.core.models import Speaker, Contact, Talk, Media

class ContactInline(admin.TabularInline):
    model = Contact
    extra = 1

class SpeakerAdmin(admin.ModelAdmin):
    inlines = [ContactInline,]
    prepopulated_fields = {'slug': ('name',)}
    
admin.site.register(Speaker, SpeakerAdmin)
admin.site.register(Talk)
admin.site.register(Media)