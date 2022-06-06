from bokeh.io import output_file, show
from bokeh.plotting import figure

#HTML file to output your plot into
output_file("bokeh.html")
# ------------------------------------
#Constructing a basic line plot

x = [5,6,7,8,9,10]
y = [1,2,3,4,5,6]

p = figure(plot_width=500, plot_height=400, tools="pan,hover", x_axis_label = "Number of times a customer has purchased a product", y_axis_label = "Quantity of product purchased")

p.line(x,y)

p.cross(x,y, size = 15)

show (p)
# ----------------------------------
#Creating a bar plot
xbar = [8,9,10]
ybar = [1,2,3]

plot = figure(x_axis_label = "Number of times a customer has purchased a product", y_axis_label = "Quantity of product purchased")

plot.vbar(xbar,top = ybar, color = "blue", width = 0.5)

output_file('barplot.html')

show(plot)
# -------------------------------
#Creating patch plot

#create the regions to a map

x_region = [[1,1,2,], [2,2,3], [2,3,5,4]]
y_region = [[2,5,6], [3,6,7], [2,4,7,8]]

plot2 = figure(x_axis_label = "Number of times a customer has purchased a product", y_axis_label = "Quantity of product purchased")

#building the patch plot

plot2.patches(x_region, y_region, fill_color = ['yellow', 'black', 'green'], line_color = 'white')

#output the plot

output_file('patch_plot.html')

show(plot2)

# -----------------------------
#Creating Scatter Plots

plot3 = figure(x_axis_label = "Number of times a customer has purchased a product", y_axis_label = "Quantity of product purchased")

#creating the x and y points

xplot = [1,2,3,4,5]
yplot = [5,7,2,2,4]

#plotting points with a circle marker

plot3.circle(xplot,yplot, size = 30, alpha = 0.5)

#output the plot
output_file('scatter.html')

show(plot3)