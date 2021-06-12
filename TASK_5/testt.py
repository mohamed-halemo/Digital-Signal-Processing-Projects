from bokeh.layouts import row,column
from bokeh.palettes import RdYlBu3

from bokeh.plotting import figure, output_file, show, Column,curdoc
from bokeh.models import DataTable, TableColumn, PointDrawTool, ColumnDataSource
from math import *
from cmath import*
 
""" To Run the file ( python -m bokeh serve --show testt.py) in the terminal   """

s1 = figure(plot_width=300, plot_height=300,x_range=(-1.5, 1.5), y_range=(-1.5, 1.5),toolbar_location="below")
s1.circle(x=[0], y=[0], color="grey",
              radius=1,alpha=0.3 )
#######################ZERO###############################################
source = ColumnDataSource({
    'x-axis of zeros': [0], 'y-axis of zeros': [0], 'color of zeros': ['red']
})

renderer = s1.scatter(x='x-axis of zeros', y='y-axis of zeros', source=source, color='color of zeros', size=10)
columns = [TableColumn(field="x-axis of zeros", title="x-axis of zeros"),
           TableColumn(field="y-axis of zeros", title="y-axis of zeros")
           ]
table = DataTable(source=source, columns=columns, editable=True, height=200)
############################poles#########################################
source_2 = ColumnDataSource({
    'x-axis of poles': [0], 'y-axis of poles': [1], 'color': ['blue']
})

renderer_2 = s1.asterisk(x='x-axis of poles', y='y-axis of poles', source=source_2, color='color', size=10)
columns_2 = [TableColumn(field="x-axis of poles", title="x-axis of poles"),
           TableColumn(field="y-axis of poles", title="y-axis of poles")
           ]
table_2 = DataTable(source=source_2, columns=columns_2, editable=True, height=200)
#########################################################################################
draw_tool = PointDrawTool(renderers=[renderer], empty_value='red')
draw_tool_2 = PointDrawTool(renderers=[renderer_2], empty_value='blue')
pole=[]
zero=[]

s1.add_tools(draw_tool,draw_tool_2)
s1.toolbar.active_tap = draw_tool
s2 = figure(width=400, height=400, title=None)
s2.toolbar.logo = None
s2.toolbar_location = None
plot=Column(s1,s2)
curdoc().add_root(row(plot,table,table_2))
