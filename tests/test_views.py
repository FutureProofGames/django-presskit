# -*- coding: utf-8 -*-
from django.urls import reverse
from django.test import TestCase, Client

from django_presskit.models import Company, Project,\
    MonetizationPermission

class GeneralViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        comp = Company.objects.create(title='Test Company',
            slug='test-company',
            description='Description',
            address='Place')
        perms = MonetizationPermission.objects.create(option='Test Permission')
        cls.project = Project.objects.create(title='Test Project',
            slug='test-project',
            press_can_request_copy=True,
            company=comp,
            monetization_permission=perms,
            website='example.com')
        cls.client = Client()

    def test_bad_company_redirects(self):
        response = self.client.get(reverse('django_presskit:company', kwargs={'company_slug': 'NotACompany'}))
        self.assertRedirects(response, reverse('django_presskit:default'))

    def test_bad_project_redirects(self):
        response = self.client.get(reverse('django_presskit:project', kwargs={'project_slug': 'NotAProject'}))
        self.assertRedirects(response, reverse('django_presskit:default'))

    def test_load_project(self):
        response = self.client.get(reverse('django_presskit:project',
                                           kwargs={'project_slug': self.project.slug}))
        self.assertContains(
            response, self.project.website, status_code=200)

    def test_load_project_xml(self):
        response = self.client.get(reverse('django_presskit:project_xml',
                                           kwargs={'project_slug': self.project.slug}))
        self.assertContains(
            response, self.project.website, count=1, status_code=200)

    def test_project_header_no_image_raises_404(self):
        response = self.client.get(reverse('django_presskit:project_header',
                                   kwargs={'project_slug': self.project.slug}))
        self.assertEquals(response.status_code, 404)
