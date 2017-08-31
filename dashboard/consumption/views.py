# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *
import datetime
# Create your views here.


def summary(request):
  users = UserData.objects.all()
  paginator = Paginator(users, 5)
  page = request.GET.get('page')
  try:
      users = paginator.page(page)
  except PageNotAnInteger:
      # If page is not an integer, deliver first page.
      users = paginator.page(1)
  except EmptyPage:
      # If page is out of range (e.g. 9999), deliver last page of results.
      users = paginator.page(paginator.num_pages)

  aggregations = Aggregation.objects.all().order_by('date')
  if len(aggregations) > 5:
      #return 5 equally distant aggregation dates
      date_first = aggregations.first().date
      date_last = aggregations.last().date

      days_diff = (date_last-date_first).days

      diff= days_diff/5;
      dates=[]
      for i in range(0,5):
          dates.insert(i,date_first + i* datetime.timedelta(days=diff) )
      aggregations = Aggregation.objects.filter(date__in=dates).order_by('date')
  else:
      aggregations = Aggregation.objects.all().order_by('date')
  return render(request, 'consumption/summary.html', { 'users': users, 'aggregations': aggregations })

def detail(request, pk):
  user = get_object_or_404(UserData, pk=pk)
  consumptions = Consumption.objects.filter(user = user)
  if len(consumptions) > 5:
      #return 5 equally distant date times
      datetime_first = consumptions.first().datetime
      datetime_last = consumptions.last().datetime

      datetime_diff = (datetime_last-datetime_first).seconds

      diff=  datetime_diff/5;
      datetimes=[]
      for i in range(0,5):
          datetimes.insert(i,datetime_first + i* datetime.timedelta(seconds=diff) )
      consumptions = Consumption.objects.filter(datetime__in=datetimes, user = user)
  else:
      consumptions = Consumption.objects.filter(user=user)
  return render(request, 'consumption/detail.html', { 'user' : user, 'consumptions': consumptions })
