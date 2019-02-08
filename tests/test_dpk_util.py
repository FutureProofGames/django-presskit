# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, Client
from django.urls import reverse

from django_presskit.templatetags import dpk_util
from django_presskit.models import Company, Project,\
    MonetizationPermission


class MarkdownFilterTests(TestCase):

    def test_filter(self):
        text = '_hello_ & &amp; <span>hi</span> congratulations'
        expected = '<p><em>hello</em> &amp; &amp; <span>hi</span> congratulations</p>'
        self.assertEqual(dpk_util.markdown_filter(text), expected)


class ProtocolFilterTests(TestCase):

    def test_filter_with_empty_string(self):
        text = ''
        expected = ''
        self.assertEqual(dpk_util.with_protocol(text), expected)

    def test_filter_with_protocol(self):
        text = 'https://test.com'
        expected = 'https://test.com'
        self.assertEqual(dpk_util.with_protocol(text), expected)

    def test_filter_without_protocol(self):
        text = 'test.com'
        expected = '//test.com'
        self.assertEqual(dpk_util.with_protocol(text), expected)


class DomainFilterTests(TestCase):

    def test_filter_with_empty_string(self):
        text = ''
        expected = ''
        self.assertEqual(dpk_util.domain(text), expected)

    def test_filter_with_protocol(self):
        text = 'https://test.com'
        expected = 'test.com'
        self.assertEqual(dpk_util.domain(text), expected)

    def test_filter_without_protocol(self):
        text = 'test.com'
        expected = 'test.com'
        self.assertEqual(dpk_util.domain(text), expected)


class AbsoluteUrlTagTests(TestCase):

    def setUp(self):
        comp = Company.objects.create(title='Test Company',
            slug='test-company',
            description='Description',
            address='Place')
        perms = MonetizationPermission.objects.create(option='Test Permission')
        self.project = Project.objects.create(title='Test Project',
            slug='test-project',
            press_can_request_copy=True,
            company=comp,
            monetization_permission=perms)

    def test_tag(self):
        c = Client()
        response = c.get(reverse('django_presskit:company', kwargs={'company_slug': 'test-company'}))
        expected = '"@id": "http://testserver/projects/test-project/"'
        print response.content
        self.assertContains(response, expected)
