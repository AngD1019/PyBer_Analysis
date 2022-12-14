#!/usr/bin/env python
# coding: utf-8

# # Pyber Challenge

# ### 4.3 Loading and Reading CSV files

# In[1]:


# Add Matplotlib inline magic command
get_ipython().run_line_magic('matplotlib', 'inline')
# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd

# File to Load (Remember to change these)
city_data_to_load = "..\\Resources\\city_data.csv"
ride_data_to_load = "..\\Resources\\ride_data.csv"

# Read the City and Ride Data
city_data_df = pd.read_csv(city_data_to_load)
ride_data_df = pd.read_csv(ride_data_to_load)


# ### Merge the DataFrames

# In[2]:


# Combine the data into a single dataset
pyber_data_df = pd.merge(ride_data_df, city_data_df, how="left", on=["city", "city"])

# Display the data table for preview
pyber_data_df.head()


# ## Deliverable 1: Get a Summary DataFrame 

# In[3]:


#  1. Get the total rides for each city type
total_rides = pyber_data_df.groupby(["type"]).count()["ride_id"]
total_rides.head()


# In[4]:


# 2. Get the total drivers for each city type
total_drivers = city_data_df.groupby(["type"]).sum()["driver_count"]
total_drivers


# In[5]:


#  3. Get the total amount of fares for each city type
total_fares = pyber_data_df.groupby(["type"]).sum()["fare"]
total_fares


# In[6]:


#  4. Get the average fare per ride for each city type. 
avg_ride_fare = total_fares / total_rides
avg_ride_fare


# In[7]:


# 5. Get the average fare per driver for each city type. 
avg_driver_fare = total_fares / total_drivers
avg_driver_fare.head()
 


# In[8]:


#  6. Create a PyBer summary DataFrame. 
pyber_summary_df = pd.DataFrame({
            "Total Rides" : total_rides,
            "Total Drivers" : total_drivers,
            "Total Fares" : total_fares,
            "Average Fare per Ride" : avg_ride_fare,
            "Average Fare per Driver" : avg_driver_fare})

pyber_summary_df


# In[9]:


#  7. Cleaning up the DataFrame. Delete the index name
pyber_summary_df.index.name = None
print(pyber_summary_df)


# In[10]:


#  8. Format the columns.
pyber_summary_df["Total Rides"] = pyber_summary_df["Total Rides"].map("{:.0f}".format)

pyber_summary_df["Total Drivers"] = pyber_summary_df["Total Drivers"].map("{:.0f}".format)

pyber_summary_df["Total Fares"] = pyber_summary_df["Total Fares"].map('${:,.2f}'.format)

pyber_summary_df["Average Fare per Ride"] = pyber_summary_df["Average Fare per Ride"].map('${:,.2f}'.format)

pyber_summary_df["Average Fare per Driver"] = pyber_summary_df["Average Fare per Driver"].map('${:,.2f}'.format)

pyber_summary_df


# ## Deliverable 2.  Create a multiple line plot that shows the total weekly of the fares for each type of city.

# In[11]:


#Read DataFrame
pyber_data_df


# In[12]:


# 1. create a new DataFrame with multiple indices 
#using the groupby() function on the "type" and "date" columns of the pyber_data_df DataFrame, 
#then apply the sum() method on the "fare" column to show the total fare amount for each date

new_pyber_df = pyber_data_df.groupby(["type","date"]).sum()["fare"]
new_pyber_df


# In[13]:


# 2. Reset the index on the DataFrame you created in #1. This is needed to use the 'pivot()' function.
# df = df.reset_index()
new_pyber_df = new_pyber_df.reset_index()


# In[14]:


# 3. use the pivot() function to convert the DataFrame from the previous step
#so that the index is the "date," each column is a city "type," and the values are the "fare."
new_pyber_df = new_pyber_df.pivot(index ='date',columns = 'type', values = 'fare')
new_pyber_df


# In[15]:


# 4. Create a new DataFrame from the pivot table DataFrame using loc on the given dates, '2019-01-01':'2019-04-29'.
jan_to_apr_dates = new_pyber_df.loc["2019-01-01":"2019-04-29"] 
jan_to_apr_dates


# In[16]:


# 5. Set the "date" index to datetime datatype. This is necessary to use the resample() method in Step 8.
# df.index = pd.to_datetime(df.index)

jan_to_apr_dates.index = pd.to_datetime(jan_to_apr_dates.index)


# In[20]:


# 6. Check that the datatype for the index is datetime using df.info()
jan_to_apr_dates.info()


# In[22]:


# 7. Create a new DataFrame using the "resample()" function by week 'W' and get the sum of the fares for each week.
weekly_fare_sum = jan_to_apr_dates.resample('W').sum()
weekly_fare_sum.head(10)


# In[24]:


# 8. Using the object-oriented interface method, plot the resample DataFrame using the df.plot() function. 
weekly_fare_sum.plot(figsize = (15,5))
# Import the style from Matplotlib.
from matplotlib import style
# Use the graph style fivethirtyeight.
style.use('fivethirtyeight')

style.use('fivethirtyeight')
plt.title("Total Fare by City Type")
plt.ylabel("Fare ($USD)")

plt.savefig("..\\Resources\\PyBer_fare_summary.png",dpi= 300, bbox_inches='tight')


# In[ ]:




