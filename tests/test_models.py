# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from django_presskit.models import Company, Project

class CompanyModelTests(TestCase):

    def test_company_url(self):
        comp = Company(title='Test Company', slug='test-company')
        self.assertEqual(comp.get_absolute_url(), '/test-company/')

class ProjectModelTests(TestCase):

    def test_project_url(self):
        comp = Company(title='Test Company', slug='test-company')
        proj = Project(title='Test Project', slug='test-project', company=comp)
        self.assertEqual(proj.get_absolute_url(), '/projects/test-project/')
