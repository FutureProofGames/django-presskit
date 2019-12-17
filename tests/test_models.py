# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from builtins import str
from django.test import TestCase

from django_presskit.models import Company, Project, AdditionalLink,\
    Award, Contact, Credit, Feature, MonetizationPermission, Platform,\
    Price, Quote, Social


class AdditionalLinkModelTests(TestCase):

    def test_unicode(self):
        link = AdditionalLink(title='Test Link', website='https://test.com')
        self.assertEqual(str(link), 'Test Link https://test.com')


class AwardModelTests(TestCase):

    def test_unicode(self):
        award = Award(description='Test Award')
        self.assertEqual(str(award), 'Test Award')


class CompanyModelTests(TestCase):

    def test_company_url(self):
        comp = Company(title='Test Company', slug='test-company')
        self.assertEqual(comp.get_absolute_url(), '/test-company/')

    def test_unicode(self):
        comp = Company(title='Test Company', slug='test-company')
        self.assertEqual(str(comp), 'Test Company')


class ContactModelTests(TestCase):

    def test_unicode(self):
        contact = Contact(name='Test Contact')
        self.assertEqual(str(contact), 'Test Contact')


class CreditModelTests(TestCase):

    def test_unicode(self):
        credit = Credit(person='Test Person', role='Test Role')
        self.assertEqual(str(credit), 'Test Person, Test Role')


class FeatureModelTests(TestCase):

    def test_unicode(self):
        feature = Feature(description='Test Feature')
        self.assertEqual(str(feature), 'Test Feature')


class MonetizationPermissionModelTests(TestCase):

    def test_unicode(self):
        perms = MonetizationPermission(option='Test Permission')
        self.assertEqual(str(perms), 'Test Permission')


class PlatformModelTests(TestCase):

    def test_unicode(self):
        project = Project(title='Test Project')
        plat = Platform(project=project, name='Test Platform')
        self.assertEqual(str(plat), 'Test Project - Test Platform')


class PriceModelTests(TestCase):

    def test_unicode(self):
        project = Project(title='Test Project')
        price = Price(project=project, price='Test Price')
        self.assertEqual(str(price), 'Test Project - Test Price')


class ProjectModelTests(TestCase):

    def test_project_url(self):
        comp = Company(title='Test Company', slug='test-company')
        proj = Project(title='Test Project', slug='test-project', company=comp)
        self.assertEqual(proj.get_absolute_url(), '/projects/test-project/')

    def test_unicode(self):
        proj = Project(title='Test Project')
        self.assertEqual(str(proj), 'Test Project')


class QuoteModelTests(TestCase):

    def test_unicode(self):
        quote = Quote(reviewer='Test Person', description='Test Description',
                      website='https://test.com')
        self.assertEqual(str(quote), 'Test Person, https://test.com, Test Description')


class SocialModelTests(TestCase):

    def test_unicode(self):
        comp = Company(title='Test Company', slug='test-company')
        social = Social(company=comp, name='Test Social')
        self.assertEqual(str(social), 'Test Company Test Social')
