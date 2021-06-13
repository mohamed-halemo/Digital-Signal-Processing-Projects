from bokeh.layouts import row,column
from bokeh.models.layouts import Row
from bokeh.palettes import RdYlBu3
from bokeh.plotting import figure, output_file, show, Column,curdoc
from bokeh.models import DataTable, TableColumn, PointDrawTool, ColumnDataSource,CDSView, IndexFilter
from math import *
from scipy.signal import freqz
import numpy as np
from scipy.signal import zpk2ss, ss2zpk, tf2zpk, zpk2tf
from cmath import *

""" To Run the file ( python -m bokeh serve --show testt.py) in the terminal   """

s1 = figure(plot_width=300, plot_height=300,x_range=(-1.5, 1.5), y_range=(-1.5, 1.5),toolbar_location="below")
s1.circle(x=[0], y=[0], color="grey",
              radius=1,alpha=0.3 )
MagGraph=figure(x_range=(0,3.14), y_range=(0,10), tools=[],
title='Magnitude',plot_width=400, plot_height=400)
phaseGraph=figure(x_range=(0,3.14), y_range=(0,10), tools=[],
title='Phase',plot_width=400, plot_height=400)
#######################ZERO###############################################
source = ColumnDataSource(data=dict(x_of_poles=[], y_of_poles=[]))

renderer = s1.circle(x="x_of_poles", y="y_of_poles", source=source, color='red', size=10)
columns = [TableColumn(field="x_of_poles", title="x_of_poles"),
           TableColumn(field="y_of_poles", title="y_of_poles")
           ]
table = DataTable(source=source, columns=columns, editable=True, height=200)
############################poles#########################################
source_2 = ColumnDataSource(data=dict(x_of_zeros=[], y_of_zeros=[]))

renderer_2 = s1.asterisk(x='x_of_zeros', y='y_of_zeros', source=source_2, color='blue', size=10)
columns_2 = [TableColumn(field="x_of_zeros", title="x_of_zeros"),
           TableColumn(field="y_of_zeros", title="y_of_zeros")
           ]
table_2 = DataTable(source=source_2, columns=columns_2, editable=True, height=200)
##########################################################################
source_3= ColumnDataSource({
    'h':[], 'w':[]
})
MagGraph.line(x='h',y='w',source=source_3)
def update(attr, old, new):
    ZeorsAndPoles()
source.on_change('data',update)
source_2.on_change('data',update)
global Zero,Pole
Zero = []
Pole = []
def ZeorsAndPoles():
    
    for i in range(len(source_2.data['x_of_zeros'])):
        Zero.append(source_2.data['x_of_zeros'][i]+source_2.data['y_of_zeros'][i]*1j)
    for i in range(len(source.data['x_of_poles'])):
        Pole.append(source.data['x_of_poles'][i]+source.data['y_of_poles'][i]*1j)
    
    Mag()
    
def Mag():
    source_3.data={
    'h': [], 'w': []
    }
   
    num, den=zpk2tf(Zero,Pole,1)
    w,h=freqz(num,den,worN=10000)
    mag=np.sqrt(h.real**2+h.imag**2)
    phase=np.arctan(h.imag/h.real)
    """ if len(source_2.data['x_of_zeros']) and len(source.data['x_of_poles']) ==0:
        mag=[]
        w=[]
        phase=[]
        source_3.data={'w': [], 'h': [] }
 """
    source_3.stream({
    'h': w, 'w': mag
    })
   

###########################################################################3
draw_tool = PointDrawTool(renderers=[renderer], empty_value='red')
draw_tool_2 = PointDrawTool(renderers=[renderer_2], empty_value='blue')


s1.add_tools(draw_tool,draw_tool_2)
s1.toolbar.active_tap = draw_tool
MagGraph.toolbar.logo = None
MagGraph.toolbar_location = None
phaseGraph.toolbar.logo = None
phaseGraph.toolbar_location = None
plot2=Row(MagGraph,phaseGraph)
plot=Row(s1,table,table_2)
curdoc().add_root(column(plot,plot2))
