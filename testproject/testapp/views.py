# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import datetime
from testapp.models import *


# Create your views here.
def main_view(request):
    date = datetime.datetime.now()
    return render(request, 'testapp/result.html', {'date': date})


def hyderabad_view(request):
    job_list=Hyd_Job.objects.order_by('DATE')
    my_dict={'job_list':job_list}
    return render(request, 'testapp/hyd.html',context=my_dict)


def mumbai_view(request):
    job_list = Mumbai_Job.objects.order_by('DATE')
    my_dict = {'job_list': job_list}
    return render(request, 'testapp/mumbai.html',context=my_dict)


def pune_view(request):
    job_list = Pune_Job.objects.order_by('DATE')
    my_dict = {'job_list': job_list}
    return render(request, 'testapp/pune.html',context=my_dict )


def bangalora_view(request):
    job_list = Bangalora_Job.objects.order_by('DATE')
    my_dict = {'job_list': job_list}
    return render(request, 'testapp/bangalora.html',context=my_dict )
