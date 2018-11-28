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

def presskit(request, company_slug=None):
    if not company_slug:
      try:
        company = Company.objects.get(pk=settings.DJANGO_PRESSKIT_DEFAULT_COMPANY_ID)
      except Exception as e:
        print e
        return render(request, 'django_presskit/no_default.html')
    else:
      company = Company.objects.get(slug=company_slug)
    context = {
      'request': request,
      'company': company,
    }
    return render(request, 'django_presskit/company.html', context)

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

## From https://stackoverflow.com/a/51655455
def _zipresponse(filelist, zipfilename):
    byte_data = BytesIO()
    zip_file = zipfile.ZipFile(byte_data, "w")

    for file in filelist:
        filename = os.path.basename(os.path.normpath(file))
        zip_file.write(file, filename)
    zip_file.close()

    response = HttpResponse(byte_data.getvalue(), content_type='application/zip')
    response['Content-Disposition'] = 'attachment; filename="' + zipfilename + '.zip"'

    return response


@cache_page(60 * 15)
def company_zip(request, company_slug):
    company = Company.objects.get(slug=company_slug)
    return _zipresponse(
      (file.content.path for file in company.images.all()),
      company.title
    )


@cache_page(60 * 15)
def company_logo_zip(request, company_slug):
    company = Company.objects.get(slug=company_slug)
    return _zipresponse(
      (file.content.path for file in company.logos.all()),
      company.title
    )


@cache_page(60 * 15)
def project_zip(request, project_slug):
    project = Project.objects.get(slug=project_slug)
    return _zipresponse(
      (file.content.path for file in project.images.all()),
      project.title
    )


@cache_page(60 * 15)
def project_logo_zip(request, project_slug):
    project = Project.objects.get(slug=project_slug)
    return _zipresponse(
      (file.content.path for file in project.logos.all()),
      project.title
    )
