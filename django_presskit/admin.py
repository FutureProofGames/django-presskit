# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin

from .models import AdditionalLink, Attachment, Award, Company
from .models import CompanyImageAttachment, Contact, Credit, Feature
from .models import MonetizationPermission, Platform, Price, Project, Quote
from .models import Social, Trailer, CompanyVideo, ProjectImageAttachment
from .models import ProjectLogoAttachment, CompanyLogoAttachment

class CompanyImagesInline(SortableInlineAdminMixin, admin.StackedInline):
    model = CompanyImageAttachment
    readonly_fields = ('datetime_created', 'datetime_updated',)
    extra = 1


class ProjectImagesInline(SortableInlineAdminMixin, admin.StackedInline):
    model = ProjectImageAttachment
    readonly_fields = ('datetime_created', 'datetime_updated',)
    extra = 1


class ProjectLogosInline(SortableInlineAdminMixin, admin.StackedInline):
    model = ProjectLogoAttachment
    readonly_fields = ('datetime_created', 'datetime_updated',)
    extra = 1


class CompanyLogosInline(SortableInlineAdminMixin, admin.StackedInline):
    model = CompanyLogoAttachment
    readonly_fields = ('datetime_created', 'datetime_updated',)
    extra = 1


class SocialInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Social
    readonly_fields = ('datetime_created', 'datetime_updated',)
    extra = 1


class CompanyVideoInline(SortableInlineAdminMixin, admin.StackedInline):
    model = CompanyVideo
    readonly_fields = ('datetime_created', 'datetime_updated',)
    extra = 1


class AdditionalLinkAdmin(admin.ModelAdmin):
    readonly_fields = ('datetime_created', 'datetime_updated',)
    prepopulated_fields = {"slug": ("title",)}


class AttachmentAdmin(admin.ModelAdmin):
    pass


class AwardAdmin(admin.ModelAdmin):
    readonly_fields = ('datetime_created', 'datetime_updated',)


class CompanyAdmin(admin.ModelAdmin):
    readonly_fields = ('datetime_created', 'datetime_updated',)
    filter_horizontal = (
        'additional_links', 'quotes', 'contacts', 'credits', 'awards')
    inlines = [SocialInline, CompanyImagesInline, CompanyLogosInline, CompanyVideoInline]
    prepopulated_fields = {"slug": ("title",)}


class ContactAdmin(admin.ModelAdmin):
    readonly_fields = ('datetime_created', 'datetime_updated',)


class CreditAdmin(admin.ModelAdmin):
    readonly_fields = ('datetime_created', 'datetime_updated',)


class MonetizationPermissionAdmin(admin.ModelAdmin):
    readonly_fields = ('datetime_created', 'datetime_updated',)


class FeatureInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Feature
    readonly_fields = ('datetime_created', 'datetime_updated',)
    extra = 1


class PlatformInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Platform
    readonly_fields = ('datetime_created', 'datetime_updated',)
    extra = 1


class PriceInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Price
    readonly_fields = ('datetime_created', 'datetime_updated',)
    extra = 1


class TrailerInline(SortableInlineAdminMixin, admin.StackedInline):
    model = Trailer
    readonly_fields = ('datetime_created', 'datetime_updated',)
    extra = 1


class ProjectAdmin(SortableAdminMixin, admin.ModelAdmin):
    readonly_fields = ('datetime_created', 'datetime_updated',)
    filter_horizontal = (
        'additional_links', 'quotes', 'contacts', 'credits', 'awards')
    inlines = [FeatureInline, PriceInline, PlatformInline,
        ProjectLogosInline, ProjectImagesInline, TrailerInline]
    prepopulated_fields = {"slug": ("title",)}


class QuoteAdmin(admin.ModelAdmin):
    readonly_fields = ('datetime_created', 'datetime_updated',)


admin.site.register(AdditionalLink, AdditionalLinkAdmin)
admin.site.register(Attachment, AttachmentAdmin)
admin.site.register(Award, AwardAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Credit, CreditAdmin)
admin.site.register(MonetizationPermission, MonetizationPermissionAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Quote, QuoteAdmin)
