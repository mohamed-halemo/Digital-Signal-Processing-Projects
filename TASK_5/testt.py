from bokeh.layouts import row,column
from bokeh.palettes import RdYlBu3
from bokeh.plotting import figure, output_file, show, Column,curdoc
from bokeh.models import DataTable, TableColumn, PointDrawTool, ColumnDataSource,CDSView, IndexFilter
from math import *
from cmath import *


s1 = figure(plot_width=300, plot_height=300,x_range=(-1.5, 1.5), y_range=(-1.5, 1.5),toolbar_location="below")
s1.circle(x=[0], y=[0], color="grey",
              radius=1,alpha=0.3 )
#######################ZERO###############################################
source = ColumnDataSource(data=dict(x_of_poles=[0.5], y_of_poles=[0.5]))

renderer = s1.asterisk(x="x_of_poles", y="y_of_poles", source=source, color='red', size=10)
columns = [TableColumn(field="x_of_poles", title="x_of_poles"),
           TableColumn(field="y_of_poles", title="y_of_poles")
           ]
table = DataTable(source=source, columns=columns, editable=True, height=200)
############################poles#########################################
source_2 = ColumnDataSource(data=dict(x_of_zeros=[0], y_of_zeros=[0]))

renderer_2 = s1.circle(x='x_of_zeros', y='y_of_zeros', source=source_2, color='blue', size=10)
columns_2 = [TableColumn(field="x_of_zeros", title="x_of_zeros"),
           TableColumn(field="y_of_zeros", title="y_of_zeros")
           ]
table_2 = DataTable(source=source_2, columns=columns_2, editable=True, height=200)
##########################################################################
draw_tool = PointDrawTool(renderers=[renderer], empty_value='red')
draw_tool_2 = PointDrawTool(renderers=[renderer_2], empty_value='blue')
pole=[]
zero=[]

s1.add_tools(draw_tool,draw_tool_2)
s1.toolbar.active_tap = draw_tool
s2 = figure(width=300, height=300, title=None)
s2.toolbar.logo = None
s2.toolbar_location = None
plot=Column(s1,s2)
curdoc().add_root(row(plot,table,table_2))
