from django.core.management.base import BaseCommand
from consumption.models import *
from django.db.models import Sum, Avg
class Command(BaseCommand):
  help = 'Aggregates consumption data'
  def handle(self, *args, **options):
      print("Aggregating consumption data. This might take a few minutes...")
      consumptions = Consumption.objects.all()
      date_list = list(set([element.datetime.date() for element in consumptions]))
      if not consumptions:
          print("No user consumption data to aggregate.")
      else:
          data = []
          date_seens = set()
          for date in date_list:
              if date not in date_seens:
                  all = Consumption.objects.filter(datetime__date = date).aggregate(Sum('consumption'), Avg('consumption'))
                  data.append(Aggregation(date = date, total = all['consumption__sum'], average = all['consumption__avg']))
                  date_seens.add(date)
          Aggregation.objects.bulk_create(data)
          print("Aggregation consumption data complete!")

