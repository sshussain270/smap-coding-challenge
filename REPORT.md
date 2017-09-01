# Report

 - [Importing user and consumption data](#Importing-user-and-consumption-data)
 - [Aggregating consumption data](#Aggregating-consumption-data)
 - [Updates to user interface](#Updates-to-user-interface)
   - [Summary View](##Summary-View)
   - [Detail View](##Detail-View)
 - [Tests](#Tests)
 
 # Importing user and consumption data
 
Import.py command has been updated in dashboard/consumption/management/commands/import.py. You can import both user and consumption data using:

    python manage.py import
    
It imports all user data from data/user_data.csv file to the database and then for each user imported into database, it imports all consumption data from data/consumption/(user id).csv. When adding new files, make sure you place the new data files in the directories specified.

**NOTE:** Django uses naive and aware datetime objects for time related data and functions. The information collected from the CSV files contains datetime from a timezone that the system is not aware of. Therefore, with each collected row, it displays a runtime warning  stating that the object is using naive datetime while the time zone in settings is set to True. Since the system doesn't use timezone functions for anything currently, I have silenced the warnings by setting USE_TZ = False in dashboard/settings.py. However, in future if you wish to use timezone functions, you can always set it to USE_TZ = True.
 
 
 # Aggregating consumption data
 
 Aggregate.py command has ben added in dashboard/consumption/management/commands/aggregate.py. You can aggregate consumption data for all users using:
 
     python manage.py aggregate
     
It calculates average and sum total of data for all users' consumption and stores it in database through a seperate model called Aggregation while the orignal user records are kept the same.
 
 
 # Updates to user interface
 
 The user interface has been updated to include the following.
 
 ## Summary View
 
 Summary.html now shows:
 
 1. A table containing user information: id, area, tariff and link to open detail view of the user. Pagination is implemented and summary page only displays 5 users in a single page to keep the page load to minimum.
 
 2. A line chart showing aggregation of the total consumption of all users over a period of dates. The dates are minified to 5 equally distant dates from the total records in the database to keep the chart load to minimum. [ChartJS library](http://www.chartjs.org/) has been used to display charts. I have used cdnjs links in header which are protected linked to externally stored secure files (https://cdnjs.com/libraries/Chart.js).
 
 **NOTE:** I have implemented two different charts for Average and Total consumption due to large difference between the values of two.
 
 ## Detail View
 
 The detail view shows 
 
 1. Details of the user: user id, area, tariff
 
 2. A line chart showing the consumption of the user over a period of datetime. The datetimes are minified to 5 equally distant dates from the total records in the database to keep the chart load to minimum.
 
 # Tests

The following tests have been implemented using Django's [UnitTest](https://docs.python.org/3/library/unittest.html#module-unittest) library:

1. Test Case for Models: UserData, Consumption, Aggregation

2. Test Case for Commands: import.py, aggregate.py

3. Test Case for Views: summary.html, detail.html





