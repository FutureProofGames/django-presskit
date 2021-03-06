# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from builtins import object
from django.db import models
from filer.fields.file import FilerFileField
from filer.fields.image import FilerImageField


class AdditionalLink(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField(null=True, blank=True)
    website = models.URLField()
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_updated = models.DateTimeField(auto_now=True)
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta(object):
        ordering = ['my_order', 'datetime_updated']

    def __str__(self):
        return self.title + ' ' + self.website

class Attachment(models.Model):
    content = FilerImageField(on_delete=models.CASCADE)

    def __str__(self):
        return self.content.url

class Award(models.Model):
    description = models.CharField(max_length=200)
    info = models.CharField(max_length=1000, null=True, blank=True)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_updated = models.DateTimeField(auto_now=True)
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta(object):
        ordering = ['my_order', 'datetime_updated']

    def __str__(self):
        return self.description


class Company(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    website = models.URLField(null=True, blank=True)
    header_image = FilerImageField(null=True, blank=True,
                                   related_name='company_header_image',
                                   on_delete=models.SET_NULL)
    based_in = models.CharField(max_length=400, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    history = models.TextField(null=True, blank=True)
    analytics = models.CharField(max_length=200, null=True, blank=True,
                                 help_text='Your Google Analytics ID')
    founding_date = models.CharField(max_length=200, null=True,
                                     blank=True)
    press_contact = models.EmailField(
        max_length=200, null=True, blank=True,
        help_text='The primary press contact email for your company')
    phone = models.CharField(max_length=50, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    additional_links = models.ManyToManyField(AdditionalLink,
                                              blank=True)
    images = models.ManyToManyField(Attachment,
                                    through='CompanyImageAttachment',
                                    related_name='company_images')
    logos = models.ManyToManyField(Attachment,
                                   through='CompanyLogoAttachment',
                                   related_name='company_logos')
    quotes = models.ManyToManyField('Quote', blank=True)
    awards = models.ManyToManyField('Award', blank=True)
    credits = models.ManyToManyField('Credit', blank=True)
    contacts = models.ManyToManyField('Contact', blank=True)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_updated = models.DateTimeField(auto_now=True)
    asset_archive = FilerFileField(blank=True, null=True,
                                   on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('django_presskit:company', kwargs={'company_slug': self.slug})

    class Meta(object):
        verbose_name_plural = 'companies'


class CompanyImageAttachment(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    attachment = models.ForeignKey(Attachment,
                                   on_delete=models.CASCADE)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_updated = models.DateTimeField(auto_now=True)
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta(object):
        ordering = ['my_order', 'datetime_updated']


class CompanyLogoAttachment(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    attachment = models.ForeignKey(Attachment,
                                   on_delete=models.CASCADE)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_updated = models.DateTimeField(auto_now=True)
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta(object):
        ordering = ['my_order', 'datetime_updated']


class CompanyVideo(models.Model):
    name = models.CharField(max_length=400)
    company = models.ForeignKey(Company, related_name='videos', on_delete=models.CASCADE)
    embed_url = models.URLField(null=True, blank=True)
    file = FilerFileField(null=True, blank=True,
                          related_name='company_video',
                          on_delete=models.SET_NULL)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_updated = models.DateTimeField(auto_now=True)
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta(object):
        ordering = ['my_order', 'datetime_updated']


class Contact(models.Model):
    name = models.CharField(max_length=300)
    website = models.URLField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_updated = models.DateTimeField(auto_now=True)
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta(object):
        ordering = ['my_order', 'datetime_updated']

    def __str__(self):
        return self.name


class Credit(models.Model):
    person = models.CharField(max_length=300)
    website = models.URLField(null=True, blank=True)
    role = models.TextField(null=True, blank=True)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_updated = models.DateTimeField(auto_now=True)
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta(object):
        ordering = ['my_order', 'datetime_updated']

    def __str__(self):
        return self.person + ', ' + self.role


class Feature(models.Model):
    description = models.CharField(max_length=1000)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_updated = models.DateTimeField(auto_now=True)
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta(object):
        ordering = ['my_order', 'datetime_updated']

    def __str__(self):
        return self.description


class MonetizationPermission(models.Model):
    option = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.option


class Platform(models.Model):
    name = models.CharField(max_length=200)
    website = models.URLField(null=True, blank=True)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_updated = models.DateTimeField(auto_now=True)
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta(object):
        ordering = ['my_order', 'datetime_updated']

    def __str__(self):
        return self.project.title + ' - ' + self.name


class Price(models.Model):
    price = models.CharField(max_length=200)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_updated = models.DateTimeField(auto_now=True)
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta(object):
        ordering = ['my_order', 'datetime_updated']

    def __str__(self):
        return self.project.title + ' - ' + self.price


class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    header_image = FilerImageField(null=True, blank=True,
                                   related_name='project_header_image',
                                   on_delete=models.SET_NULL)
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
    monetization_permission = models.ForeignKey(MonetizationPermission,
        on_delete=models.CASCADE)
    distribute_game_id = models.CharField(
        null=True, blank=True, max_length=25, help_text='The game ID from your Distribute() keyfile (https://dodistribute.com/games/presskit/THIS-ID/)')
    distribute_access_hash = models.CharField(
        null=True, blank=True, max_length=25, help_text='The access hash from your Distribute() keyfile (https://dodistribute.com/access/add/THIS-HASH/)')
    distribute_key = models.CharField(
        null=True, blank=True, max_length=80, help_text='The key from your Distribute() keyfile filename (ds_THIS-KEY)')
    quotes = models.ManyToManyField('Quote', blank=True)
    additional_links = models.ManyToManyField(AdditionalLink,
                                              blank=True)
    awards = models.ManyToManyField('Award', blank=True)
    credits = models.ManyToManyField(Credit, blank=True)
    contacts = models.ManyToManyField(Contact, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_updated = models.DateTimeField(auto_now=True)
    asset_archive = FilerFileField(blank=True, null=True,
                                   on_delete=models.SET_NULL)
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta(object):
        ordering = ['my_order', 'datetime_updated']

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('django_presskit:project', kwargs={'project_slug': self.slug})

    def __str__(self):
        return self.title


class ProjectImageAttachment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    attachment = models.ForeignKey(Attachment,
                                   on_delete=models.CASCADE)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_updated = models.DateTimeField(auto_now=True)
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta(object):
        ordering = ['my_order', 'datetime_updated']


class ProjectLogoAttachment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    attachment = models.ForeignKey(Attachment,
                                   on_delete=models.CASCADE)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_updated = models.DateTimeField(auto_now=True)
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta(object):
        ordering = ['my_order', 'datetime_updated']


class Quote(models.Model):
    reviewer = models.CharField(max_length=400)
    website = models.URLField()
    publication_name = models.CharField(max_length=400)
    description = models.TextField()
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_updated = models.DateTimeField(auto_now=True)
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta(object):
        ordering = ['my_order', 'datetime_updated']

    def __str__(self):
        return self.reviewer + ', ' + self.website + ', ' + self.description


class Social(models.Model):
    name = models.CharField(max_length=200)
    website = models.URLField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_updated = models.DateTimeField(auto_now=True)
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta(object):
        ordering = ['my_order', 'datetime_updated']

    def __str__(self):
        return self.company.title + ' ' + self.name


class Trailer(models.Model):
    name = models.CharField(max_length=400)
    embed_url = models.URLField(null=True, blank=True)
    project = models.ForeignKey(Project, related_name='videos',
                                on_delete=models.CASCADE)
    file = FilerFileField(null=True, blank=True,
                          related_name='trailer_video',
                          on_delete=models.SET_NULL)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_updated = models.DateTimeField(auto_now=True)
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta(object):
        ordering = ['my_order', 'datetime_updated']
