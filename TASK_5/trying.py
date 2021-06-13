from bokeh.layouts import row,column
from bokeh.palettes import RdYlBu3
from scipy.signal import zpk2ss, ss2zpk, tf2zpk, zpk2tf
from bokeh.plotting import figure, output_file, show, Column,curdoc
from bokeh.models import DataTable, TableColumn, PointDrawTool, ColumnDataSource
from math import *
from cmath import*
from scipy.signal import freqz
import numpy as np
 
""" To Run the file ( python -m bokeh serve --show testt.py) in the terminal   """

s1 = figure(plot_width=300, plot_height=300,x_range=(-1.5, 1.5), y_range=(-1.5, 1.5),toolbar_location="below")
s1.circle(x=[0], y=[0], color="grey",
              radius=1,alpha=0.3 )

MagGraph.line(x='w',y='h',source=source2)
#######################ZERO###############################################
source = ColumnDataSource({
   'x_zeros': [], 'y_zeros': [], 
})
source_2 = ColumnDataSource({
   'x_poles': [], 'y_poles': [], 
})

MagGraph=figure(x_range=(0,3.14), y_range=(0,10), tools=[],
           title='Magnitude',plot_width=400, plot_height=400)
source2= ColumnDataSource({
    'w':[], 'h':[]
})

x1=[0.25,0.5,0.2,0.75]
y1=[0.25,0.5,0.2,0.75]
x2=[1.25,-1.25,2,-2]
y2=[1.25,-1.25,2,-2]

renderer = s1.scatter(x='x_zeros', y='y_zeros', source=source,size=15)
renderer_2 = s1.asterisk(x='x_poles', y='y_poles', source=source_2, size=10)

MagGraph.line(x='w',y='h',source=source2)

columns = [TableColumn(field="x_zeros", title="x_zeros"),
           TableColumn(field="y_zeros", title="y_zeros")
           ]
table = DataTable(source=source, columns=columns, editable=True, height=200)

columns_2 = [TableColumn(field="x_poles", title="x_poles"),
           TableColumn(field="y_poles", title="y_poles")
           ]
table_2 = DataTable(source=source_2, columns=columns_2, editable=True, height=200)
def update(attr, old, new):
    ZeorsAndPoles()
source.on_change('data',update)

global Zero,Pole
Zero = []
Pole = []
def ZeorsAndPoles():
    
    for i in range(len(source.data['x_zeros'])):
        
            Zero.append(source.data['x_zeros'][i]+source.data['y_zeros'][i]*1j)
        
            Pole.append(source_2.data['x_poles'][i]+source_2.data['y_poles'][i]*1j)
    print("entered")
    Mag()
    
def Mag():
    source2.data={
    'w': [], 'h': []
    }
   
    num, den=zpk2tf(Zero,Pole,1)
    w,h=freqz(num,den,worN=10000)
    mag=np.sqrt(h.real**2+h.imag**2)
    phase=np.arctan(h.imag/h.real)
    if len(source.data['x_zeros']) & len(source_2.data['x_poles']) ==0:
        mag=[]
        w=[]
        phase=[]
        source2.data={'w': [], 'h': [] }

    source2.stream({
    'w': w, 'h': mag
    })
   

#########################################################################################
draw_tool = PointDrawTool(renderers=[renderer], empty_value='red')
draw_tool_2 = PointDrawTool(renderers=[renderer_2], empty_value='blue')

s1.add_tools(draw_tool,draw_tool_2)
s1.toolbar.active_tap = draw_tool

MagGraph.toolbar.logo = None
MagGraph.toolbar_location = None
plot=Column(s1,MagGraph)
curdoc().add_root(row(plot,table,table_2))
