# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import AdditionalLink, Attachment, Award, Company
from .models import CompanyImageAttachment, Contact, Credit, Feature
from .models import MonetizationPermission, Platform, Price, Project, Quote
from .models import Social, Trailer, VideoType, CompanyLogoAttachment


class CompanyImagesInline(admin.StackedInline):
    model = CompanyImageAttachment
    readonly_fields = ('datetime_created', 'datetime_updated',)
    extra = 1


class CompanyLogosInline(admin.StackedInline):
    model = CompanyLogoAttachment
    readonly_fields = ('datetime_created', 'datetime_updated',)
    extra = 1


class SocialInline(admin.TabularInline):
    model = Social
    readonly_fields = ('datetime_created', 'datetime_updated',)
    extra = 1


class AdditionalLinkAdmin(admin.ModelAdmin):
    readonly_fields = ('datetime_created', 'datetime_updated',)


class AttachmentAdmin(admin.ModelAdmin):
    pass

class AwardAdmin(admin.ModelAdmin):
    readonly_fields = ('datetime_created', 'datetime_updated',)


class CompanyAdmin(admin.ModelAdmin):
    readonly_fields = ('datetime_created', 'datetime_updated',)
    filter_horizontal = (
        'additional_links', 'quotes', 'contacts', 'credits', 'awards')
    inlines = [SocialInline, CompanyImagesInline, CompanyLogosInline]


class ContactAdmin(admin.ModelAdmin):
    readonly_fields = ('datetime_created', 'datetime_updated',)


class CreditAdmin(admin.ModelAdmin):
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


class TrailerAdmin(admin.ModelAdmin):
    readonly_fields = ('datetime_created', 'datetime_updated',)


class VideoTypeAdmin(admin.ModelAdmin):
    readonly_fields = ('datetime_created', 'datetime_updated',)


admin.site.register(AdditionalLink, AdditionalLinkAdmin)
admin.site.register(Attachment, AttachmentAdmin)
admin.site.register(Award, AwardAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Credit, CreditAdmin)
admin.site.register(Feature, FeatureAdmin)
admin.site.register(MonetizationPermission, MonetizationPermissionAdmin)
admin.site.register(Platform, PlatformAdmin)
admin.site.register(Price, PriceAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Quote, QuoteAdmin)
admin.site.register(Trailer, TrailerAdmin)
admin.site.register(VideoType, VideoTypeAdmin)
