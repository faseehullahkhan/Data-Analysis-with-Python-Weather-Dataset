import pandas as pa

data = pa.read_csv(r'C:\Users\DC\Desktop\Python\Third_Project\Weather-Data.csv')
print(data.dtypes)

# count , count karta tha unique values
# and value_counts specific column paar unique values ko non null entrances ko count karta ha
# The above two comments is just the comments i write in my own language for my understanding you can ignore it, thanks


print(data['Weather'].value_counts())
# nunique counts all the unique values of every column

# first Question is to find all the unique wind speed values in the data
speed = data['Wind Speed_km/h'].unique()
unique_speed = data['Wind Speed_km/h'].nunique()
print(unique_speed)
print(speed)


# second question is to count the number of clear weather in the weather column
clear = data['Weather'].value_counts()
print(clear['Clear'])

# or we can do this
clear = (data['Weather'] == "Clear").sum()
print(clear)

# find the number of times the wind speed was excatly 4km/h
wind_speed = (data['Wind Speed_km/h'] == 4).sum()
print(wind_speed)

# find out all the null values in the data frame
null_values = data.isnull().sum()
print(null_values)

# Rename the weather column to weather_conditions
# Wrong way
# data['Weather'] = data['Weather'].rename("Weather Conditions")
# print(data.head())

# Corrected way
data = data.rename(columns={"Weather" : "Weather_conditions"})
print(data.head())

# What is the mean visibility
mean_visibility = data['Visibility_km'].mean()
print(mean_visibility)

#what is the standard deviation of pressure of this data
std_pressure = data['Press_kPa'].std()
print(std_pressure)

# what is the variance of relative humidity in this data
relative_humidity = data['Rel Hum_%'].var()
print(relative_humidity)

# find all the instances when "Snow" was recorded
snow_instances = data[data['Weather_conditions'].str.contains('Snow' , case= False , na = False)]
print(snow_instances)


# find all the instances where the wind speed is above 24 and visibility is 25
wind_visibility_instances = data[(data['Wind Speed_km/h'] > 24) & (data['Visibility_km'] == 25)]
print(wind_visibility_instances)

# what is the mean value of each column against each "Weather Condition"?
data['Date/Time'] = pa.to_datetime(data['Date/Time'] , errors='coerce')
mean_value_of_each_Weather_conditions = data.groupby('Weather_conditions').mean()
print(mean_value_of_each_Weather_conditions)


# what is the minimum and maximum value for each column against each weather condition
min_value_of_each_Weather_conditions = data.drop(columns=['Date/Time']).groupby('Weather_conditions').agg(['min' , 'max'])
print(min_value_of_each_Weather_conditions)


# show all the records where the weather condition is fog
foggy_condition = data[data['Weather_conditions'] == 'Fog']
print(foggy_condition)


# find all the instances when "weather is clear" or "Visibilty is above 40"
clear_visibility_instances = data[(data['Weather_conditions'].str.contains('Clear' , case=False , na=False)) | (data['Visibility_km'] > 40)]
print(clear_visibility_instances)

