# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import zipfile
import os
from io import BytesIO

from django.conf import settings
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_page

from .models import Company, Project

def fallback(func):
  def decorator(*args, **kwargs):
    try:
      return func(*args, **kwargs)
    except (Company.DoesNotExist, Project.DoesNotExist) as e:
      return redirect('django_presskit:default')

  return decorator

@fallback
def presskit(request, company_slug=None):
    if not company_slug:
      try:
        company = Company.objects.get(pk=settings.DJANGO_PRESSKIT_DEFAULT_COMPANY_ID)
      except Exception as e:
        return render(request, 'django_presskit/no_default.html')
    else:
      company = Company.objects.get(slug=company_slug)
    context = {
      'request': request,
      'company': company,
    }
    return render(request, 'django_presskit/company.html', context)

@fallback
def project(request, project_slug):
    project = Project.objects.get(slug=project_slug)
    context = {
      'request': request,
      'project': project,
    }
    return render(request, 'django_presskit/project.html', context)

def project_xml(request, project_slug):
    project = Project.objects.get(slug=project_slug)
    context = {
      'project': project,
    }
    return render(request, 'django_presskit/data.xml', context, content_type='text/xml')

def project_header(request, project_slug):
    project = Project.objects.get(slug=project_slug)
    if project.header_image:
      return redirect(project.header_image.url, permanent=True)
    else:
      raise Http404("No header image for this project.")
