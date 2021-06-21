from bokeh.plotting import figure, show

# prepare some data
x_co = [-3.14,3.14]
y_co = [0,0]
x_co_1=[0,0]
y_co_1=[-10,10]
# create a new plot with a title and axis labels
p = figure(title="Simple line example", x_axis_label="x", y_axis_label="y")

# add a line renderer with legend and line thickness
p.line(x_co,y_co, legend_label="Temp.",color='black', line_width=2)
p.line(x_co_1,y_co_1, legend_label="Temp.",color='black', line_width=2)
# show the results
show(p)