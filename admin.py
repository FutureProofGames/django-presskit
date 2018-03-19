# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import AdditionalLink, Award, Company, Contact, Feature
from .models import MonetizationPermission, Platform, Price, Project
from .models import Quote, Social, Trailer, VideoType


class AdditionalLinkAdmin(admin.ModelAdmin):
    readonly_fields = ('datetime_created', 'datetime_updated',)


class AwardAdmin(admin.ModelAdmin):
    readonly_fields = ('datetime_created', 'datetime_updated',)


class CompanyAdmin(admin.ModelAdmin):
    readonly_fields = ('datetime_created', 'datetime_updated',)


class ContactAdmin(admin.ModelAdmin):
    readonly_fields = ('datetime_created', 'datetime_updated',)


class FeatureAdmin(admin.ModelAdmin):
    readonly_fields = ('datetime_created', 'datetime_updated',)


class MonetizationPermissionAdmin(admin.ModelAdmin):
    readonly_fields = ('datetime_created', 'datetime_updated',)


class PlatformAdmin(admin.ModelAdmin):
    readonly_fields = ('datetime_created', 'datetime_updated',)


class PriceAdmin(admin.ModelAdmin):
    readonly_fields = ('datetime_created', 'datetime_updated',)


class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('datetime_created', 'datetime_updated',)


class QuoteAdmin(admin.ModelAdmin):
    readonly_fields = ('datetime_created', 'datetime_updated',)


class SocialAdmin(admin.ModelAdmin):
    readonly_fields = ('datetime_created', 'datetime_updated',)


class TrailerAdmin(admin.ModelAdmin):
    readonly_fields = ('datetime_created', 'datetime_updated',)


class VideoTypeAdmin(admin.ModelAdmin):
    readonly_fields = ('datetime_created', 'datetime_updated',)


admin.site.register(AdditionalLink, AdditionalLinkAdmin)
admin.site.register(Award, AwardAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Feature, FeatureAdmin)
admin.site.register(MonetizationPermission, MonetizationPermissionAdmin)
admin.site.register(Platform, PlatformAdmin)
admin.site.register(Price, PriceAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Quote, QuoteAdmin)
admin.site.register(Social, SocialAdmin)
admin.site.register(Trailer, TrailerAdmin)
admin.site.register(VideoType, VideoTypeAdmin)
