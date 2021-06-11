from bokeh.models.markers import X
from bokeh.plotting import figure, output_file, show, Column
from bokeh.io import curdoc
from bokeh.models import DataTable, TableColumn, PointDrawTool, ColumnDataSource, renderers,Button, CustomJS,Button

# output to static HTML file
output_file("templates\Main.html")

plot = figure(plot_width=300, plot_height=300,x_range=(-1.5, 1.5), y_range=(-1.5, 1.5))
plot.circle(x=[0], y=[0], color="grey",
              radius=1,alpha=0.3 )

renderer = plot.asterisk(x=[0, 0.1], y=[0, 0.1], size=10, color="blue")
renderer_2=plot.dot(x=[0.2,0.5],y=[0.2,0.5],size=30, color="red")
draw_tool = PointDrawTool(renderers=[renderer,renderer_2], empty_value='black')
plot.add_tools(draw_tool)
plot.toolbar.active_tap = draw_tool
show(plot)







