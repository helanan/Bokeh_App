from bokeh.io import output_file, show
from bokeh.plotting import figure
import pandas as pd

#read in the data
df = pd.read_csv('all_stocks_5yr.csv')

#Filtering for apple stocks
df_apple = df[df['Name'] == 'AAL']

#converting the date column to a time series
df_apple['date'] = pd.to_datetime(df_apple['date'])

#create the time series plot

plot = figure(x_axis_type = 'datetime', x_axis_label = 'date', y_axis_label = 'High Prices')

plot.line(x = df_apple['date'], y = df_apple['high'])

#Output the plot

output_file('pandas_time.html')

show(plot)
