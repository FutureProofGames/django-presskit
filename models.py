# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from filer.fields.file import FilerFileField
from filer.fields.image import FilerImageField


class AdditionalLink(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    website = models.URLField()
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title + ' ' + self.website

class Attachment(models.Model):
    content = FilerImageField()

class Award(models.Model):
    description = models.CharField(max_length=200)
    info = models.CharField(max_length=1000, null=True, blank=True)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_updated = models.DateTimeField(auto_now=True)


class Company(models.Model):
    title = models.CharField(max_length=200)
    based_in = models.CharField(max_length=400, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    history = models.TextField(null=True, blank=True)
    analytics = models.CharField(max_length=200, null=True, blank=True)
    promoter_id = models.CharField(max_length=20, null=True,
                                   blank=True)
    founding_date = models.CharField(max_length=200, null=True,
                                     blank=True)
    press_contact = models.EmailField(max_length=200, null=True,
                                      blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    additional_links = models.ManyToManyField(AdditionalLink,
                                              blank=True)
    quotes = models.ManyToManyField('Quote', blank=True)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title


    class Meta:
        verbose_name_plural = 'companies'


class Contact(models.Model):
    name = models.CharField(max_length=300)
    website = models.URLField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name


class Credit(models.Model):
    person = models.CharField(max_length=300)
    website = models.URLField(null=True, blank=True)
    role = models.TextField(null=True, blank=True)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.person + ' ' + self.role


class Feature(models.Model):
    description = models.CharField(max_length=1000)
    project = models.ForeignKey('Project')
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.description


class MonetizationPermission(models.Model):
    option = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.option


class Platform(models.Model):
    name = models.CharField(max_length=200)
    website = models.URLField(null=True, blank=True)
    project = models.ForeignKey('Project')
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.project.title + ' - ' + self.name


class Price(models.Model):
    price = models.CharField(max_length=20)
    project = models.ForeignKey('Project')
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.project + ' - ' + self.price


class Project(models.Model):
    title = models.CharField(max_length=200)
    header_image = FilerImageField(null=True, blank=True,
                                   related_name='project_header_image')
    release_date = models.CharField(max_length=200)
    website = models.URLField()
    description = models.TextField()
    history = models.TextField()
    images = models.ManyToManyField(Attachment,
                                    through='ProjectImageAttachment',
                                    related_name='project_images')
    logos = models.ManyToManyField(Attachment,
                                   through='ProjectLogoAttachment',
                                   related_name='project_logos')
    press_can_request_copy = models.BooleanField()
    monetization_permission = models.ForeignKey(MonetizationPermission)
    promoter_id = models.CharField(max_length=20, null=True, blank=True)
    distribute_keyfile = FilerFileField(null=True, blank=True,
                                        related_name='project_distribute_keyfile')
    quotes = models.ManyToManyField('Quote', blank=True)
    additional_links = models.ManyToManyField(AdditionalLink,
                                              blank=True)
    credits = models.ManyToManyField(Credit, blank=True)
    company = models.ForeignKey(Company)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_updated = models.DateTimeField(auto_now=True)


    def __unicode__(self):
        return self.title


class ProjectImageAttachment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    attachment = models.ForeignKey(Attachment,
                                   on_delete=models.CASCADE)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_updated = models.DateTimeField(auto_now=True)


class ProjectLogoAttachment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    attachment = models.ForeignKey(Attachment,
                                   on_delete=models.CASCADE)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_updated = models.DateTimeField(auto_now=True)


class Quote(models.Model):
    reviewer = models.CharField(max_length=400)
    website = models.URLField()
    publication_name = models.CharField(max_length=400)
    description = models.TextField()
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.reviewer + ' ' + self.website


class Social(models.Model):
    name = models.CharField(max_length=200)
    website = models.URLField()
    company = models.ForeignKey(Company)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_updated = models.DateTimeField(auto_now=True)


class Trailer(models.Model):
    name = models.CharField(max_length=400)
    video_type = models.ForeignKey('VideoType')
    embed_url = models.URLField()
    file = FilerFileField(null=True, blank=True,
                          related_name='trailer_video')
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_updated = models.DateTimeField(auto_now=True)


class VideoType(models.Model):
    source = models.CharField(max_length=200)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_updated = models.DateTimeField(auto_now=True)
