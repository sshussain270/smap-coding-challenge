from django.core.management.base import BaseCommand
from consumption.models import *
from os import listdir
from os.path import isfile, join
import csv
class Command(BaseCommand):
  help = 'import data'

  def handle(self, *args, **options):
      print("Importing user data...")
      path_user_data = "../data/user_data.csv"
      with open(path_user_data) as f:
          reader = csv.reader(f)
          has_header = csv.Sniffer().has_header(f.read(1024))
          f.seek(0)  # rewind
          incsv = csv.reader(f)
          if has_header:
              next(incsv)  # skip header row
          for row in reader:
              UserData.objects.create(user_id=row[0], area= row[1], tariff= row[2])
      if not f:
          print("No user data found")
      else:
          print("User data import complete!")
      print("Importing consumption data. This might take a few seconds...")
      users = UserData.objects.all()
      if users:
          for user in users:
              path_consumption = "../data/consumption/" + str(user.user_id) + ".csv"
              with open(path_consumption) as f:
                  reader = csv.reader(f, delimiter=',')
                  header = next(reader)
                  Consumption.objects.bulk_create([Consumption(user = user, datetime=row[0], consumption= row[1]) for row in reader])

          print("Consumption data import complete!")
      else:
          print("No user data to import consumption for.")          
