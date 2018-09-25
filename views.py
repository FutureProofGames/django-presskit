# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import zipfile
import os
from io import BytesIO

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_page

from .models import Company, Project

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

def project(request, project_id):
    project = Project.objects.get(pk=project_id)
    context = {
      'project': project,
    }
    return render(request, 'django_presskit/project.html', context)


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
def company_zip(request, company_id):
    print "Generating ZIP!"
    company = Company.objects.get(pk=company_id)
    return _zipresponse(
      (file.content.path for file in company.images.all()),
      company.title
    )


@cache_page(60 * 15)
def company_logo_zip(request, company_id):
    print "Generating ZIP!"
    company = Company.objects.get(pk=company_id)
    return _zipresponse(
      (file.content.path for file in company.logos.all()),
      company.title
    )


@cache_page(60 * 15)
def project_zip(request, project_id):
    print "Generating ZIP!"
    project = Project.objects.get(pk=project_id)
    return _zipresponse(
      (file.content.path for file in project.images.all()),
      project.title
    )


@cache_page(60 * 15)
def project_logo_zip(request, project_id):
    print "Generating ZIP!"
    project = Project.objects.get(pk=project_id)
    return _zipresponse(
      (file.content.path for file in project.logos.all()),
      project.title
    )
