from django.core.management.base import BaseCommand
from consumption.models import *
from django.db.models import Sum, Avg
class Command(BaseCommand):
  help = 'Aggregates consumption data'
  def handle(self, *args, **options):
      print("Aggregating consumption data...")
      consumptions = Consumption.objects.all()
      if not consumptions:
          print("No user consumption data to aggregate.")
      else:
          for consumption in consumptions:
              all = Consumption.objects.filter(datetime__date = consumption.datetime.date())
              total = all.aggregate(Sum('consumption'))
              average = all.aggregate(Avg('consumption'))
              date_exists = Aggregation.objects.filter(date = consumption.datetime.date())
              if not date_exists:
                  Aggregation.objects.create(date = consumption.datetime.date(), total = total['consumption__sum'], average = average['consumption__avg'])
              else:
                  data = Aggregation.objects.get(date = consumption.datetime.date())
                  data.total = total['consumption__sum']
                  data.average = average['consumption__avg']
                  data.save()
          print("Aggregation consumption data complete!")

