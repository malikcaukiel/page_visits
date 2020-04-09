##################################### Page Visits #####################################################
import pandas as pd
user_visits = pd.read_csv('page_visits.csv')

# Part 1.
# Inspecting the data
print(user_visits.head(10))

# Part 2.
# The column utm_source contains information about how users got to website's homepage
# calculating how many visits came from each of the different sources.
click_source = user_visits.groupby('utm_source').id.count().reset_index()
print(click_source)

#Part 3.
# calculating the number of visits to our site from each utm_source for each month, to check if the traffic has been changing on a monthly basis.
#click_source_by_month = user_visits.groupby(['utm_source', 'month']).first_name.count().reset_index()
click_source_by_month = user_visits.groupby(['utm_source', 'month']).id.count().reset_index()
print(click_source_by_month)

#Part 5.
# Using pivot to create a pivot table where the rows are utm_source and the columns are months.
#click_source_by_month_pivot = click_source_by_month.pivot(   
#    columns = 'month',
#    index = 'utm_source',
#    values = 'first_name').reset_index()

click_source_by_month_pivot = click_source_by_month.pivot(      
    columns = 'month',                                          
    index = 'utm_source',
    values = 'id').reset_index()
print(click_source_by_month_pivot)
#######################################################################################################
