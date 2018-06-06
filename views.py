# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.conf import settings

from .models import Company

def presskit(request, company_id=None):
    if not company_id:
      try:
        company_id = settings.DJANGO_PRESSKIT_DEFAULT_COMPANY_ID
      except:
        return render(request, 'django_presskit/no_default.html')

    company = Company.objects.get(pk=company_id)
    context = {
      'company': company,
    }
    return render(request, 'django_presskit/company.html', context)

def project(request):
    pass
