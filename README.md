# Bokeh_App
Bokeh app built from scratch

Please make sure you have the following dependecies in order to use Bokeh and launch the app.  Dependencies you should have installed are as follows:
 - Numpy
 - Jinja2
 - Six
 - Requests
 - Tornado >= 4.0
 - PyYaml
 - DateUtil

 If you are using Anaconda for distribution you can use the following commands to install from your command line:
  - conda install bokeh
  - pip install bokeh (if using pip)
  - pip3 install bokeh (if using pip3)

  After installation please verify it is correctly installed, you may use a Jupyter Notebook to do so and can install Jupyter at the following website:
  - http://jupyter.org/install
  
 To test you can generate a simple line plot with the following code: 
```
from bokeh.plotting import figure, output_file, show
#HTML file to output your plot into
output_file ("bokeh.html")

#Constructing a basic line plot

x = [1,2,3]
y = [4,5,6]

p = figure()

p.line(x,y)

show(p)
```


Please do the following to launch app locally:
Run in terminal the following: 
```bokeh serve --show {filename}.py```
