# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import *
from django.core.management import call_command
from django.db.models import Sum, Avg
# Create your tests here.
class ModelsTestCase(TestCase):
    def test_UserData(self):
        UserData.objects.create(user_id=1, area="London", tariff="241")
        UserData.objects.get(user_id=1)
    def test_Consumption(self):
        UserData.objects.create(user_id=1, area="London", tariff="241")
        user_data = UserData.objects.first()
        Consumption.objects.create(user=user_data, datetime="2016-07-15 00:00:00", consumption="39.2")
        Consumption.objects.get(user=user_data)
    def test_Aggregation(self):
        UserData.objects.create(user_id=1, area="London", tariff="241")
        user_data = UserData.objects.first()
        Consumption.objects.create(user=user_data, datetime="2016-07-15 00:00:00", consumption="39.2")
        consumption = Consumption.objects.first()
        all = Consumption.objects.filter(datetime__date = consumption.datetime.date())
        total = all.aggregate(Sum('consumption'))
        average = all.aggregate(Avg('consumption'))
        Aggregation.objects.create(date = consumption.datetime.date(), total = total['consumption__sum'], average = average['consumption__avg'])
        Aggregation.objects.get(date = consumption.datetime.date())

class CommandsTestCase(TestCase):
    def test_import(self):
        "Test import command"

        args = []
        opts = {}
        call_command('fix import', *args, **opts)
    def test_aggregate(self):
        "Test aggregate command"
        args = []
        opts = {}
        call_command('fix aggregate', *args, **opts)


class ViewsTestCase(TestCase):
    def test_call_view_summary(self):
        response = self.client.get('/summary/', follow=True)
        self.assertEqual(response.status_code, 200)
    def test_call_view_detail(self):
        UserData.objects.create(user_id=1, area="London", tariff="241")
        test_user = UserData.objects.all().first()
        response = self.client.get('/detail/' + str(test_user.pk) + '/', follow=True)
        self.assertEqual(response.status_code, 200)

