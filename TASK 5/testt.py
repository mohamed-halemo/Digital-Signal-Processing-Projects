from bokeh.models.markers import X
from bokeh.plotting import figure, output_file, show, Column
from bokeh.io import curdoc
from bokeh.models import DataTable, TableColumn, PointDrawTool, ColumnDataSource, renderers,Button, CustomJS,Button
from bokeh.layouts import column
# output to static HTML file
output_file("templates\Main.html")

plot = figure(plot_width=300, plot_height=300,x_range=(-1.5, 1.5), y_range=(-1.5, 1.5))
plot.circle(x=[0], y=[0], color="grey",
              radius=1,alpha=0.3 )
renderer_2=plot.dot(x=[],y=[],size=30, color="red")
renderer = plot.asterisk(x=[], y=[], size=10, color="blue")
draw_tool = PointDrawTool(renderers=[renderer_2], empty_value='black')
draw_tool_2 = PointDrawTool(renderers=[renderer], empty_value='black')

plot.add_tools(draw_tool,draw_tool_2)
plot.toolbar.active_tap = draw_tool
show(column(plot))







