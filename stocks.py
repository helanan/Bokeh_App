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
#----------------------------Scatter Plot with Pandas---------------

#create the scatter plot

plot_scatter = figure()

plot_scatter.circle(x = df_apple['high'], y = df_apple['low'], color = 'red', size = 10, alpha = 0.8)

plot_scatter.diamond(x = df_apple['open'], y = df_apple['close'], color = 'green', size = 10, alpha = 0.8)

#Output the plot

output_file('pandas_scatter.html')
show(plot_scatter)

#----------------Plotting with ColumnDataSource--------------
