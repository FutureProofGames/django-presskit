# -*- coding: utf-8 -*-
from django.urls import reverse
from django.test import TestCase, Client

class GeneralViewTests(TestCase):

    def test_bad_company_redirects(self):
        c = Client()
        response = c.get(reverse('django_presskit:company', kwargs={'company_slug': 'NotACompany'}))
        self.assertRedirects(response, reverse('django_presskit:default'))

    def test_bad_project_redirects(self):
        c = Client()
        response = c.get(reverse('django_presskit:project', kwargs={'project_slug': 'NotAProject'}))
        self.assertRedirects(response, reverse('django_presskit:default'))
