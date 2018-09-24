# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.conf import settings

from .models import Company, Project

def presskit(request, company_slug=None):
    if not company_id:
      try:
        company = Company.objects.get(settings.DJANGO_PRESSKIT_DEFAULT_COMPANY_ID)
      except:
        return render(request, 'django_presskit/no_default.html')
    else:
      company = Company.objects.get(slug=company_slug)
    context = {
      'company': company,
    }
    return render(request, 'django_presskit/company.html', context)

def project(request, project_slug):
    project = Project.objects.get(slug=project_slug)
    context = {
      'project': project,
    }
    return render(request, 'django_presskit/project.html', context)
