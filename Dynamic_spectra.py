from bokeh.plotting import figure, curdoc
import pandas as pd
from bokeh.models import ColumnDataSource,ColorBar
from bokeh.models.tools import *
from bokeh.models import CustomJS,LinearColorMapper, Label
import numpy as np
import os, sys, time, subprocess, commands
from bokeh.transform import LinearColorMapper
from bokeh.palettes import Spectral6

#A=sys.argv[3]
#B=sys.argv[4]

filename=sys.argv[2]

plots=pd.read_csv(filename,delim_whitespace=True,header =None)

#print filename   
 
def time_dm(attr,old,new):
    inds=new
    box_name=source.data['Time'][inds]
    sec_name=source.data['DM'][inds]
    df1  = box_name.to_frame()
    df2  = sec_name.to_frame() 
    time= df1.iloc[:,0].values
    dm= df2.iloc[:,0].values
    print time
    print dm 
    for x,y in zip(time,dm):
          skip=x-0.2
          print "Time of pulse: %s"%x
          print "Extract from: %s"%skip
          command="dspsr -c 0.4 -cepoch start -S"+" "+str(skip)+" "+"-T 0.4 -D"+" "+str(x)+" "+"-O"+" "+str(x)+"_"+str(y)+"_burst.ar"+" "+str(rawdata) 
          subprocess.check_output(command, shell= True)
          output=commands.getoutput(command)
          output2=commands.getoutput("ls -1rt | tail -1")
          
          print command
          
          pazi=commands.getoutput("pazi %s"%output2)
         
       
S=plots[1]

d=plots[1].values
#A=low=min(d)
#B=high=max(d)

source=ColumnDataSource(dict(Time=plots[2],DM=plots[0],S=plots[1]))

TOOLS="pan,wheel_zoom,reset,hover,poly_select,box_select"

color_mapper1 = LinearColorMapper(palette='Magma256', low=min(d), high=max(d))





p = figure(plot_width=500,plot_height=500,title="Some Figure",y_range=(500,1000),tools=TOOLS)

r=p.scatter('Time','DM',size=3, color={'field': 'S', 'transform': color_mapper1},source=source)

color_bar = ColorBar(color_mapper=color_mapper1, title='',
                            #title=color.value.title(),
                            title_text_font_style='bold',
                            title_text_font_size='20px',
                            title_text_align='center',
                            orientation='vertical',
                            major_label_text_font_size='16px',
                            major_label_text_font_style='bold',
                            label_standoff=8,
                            major_tick_line_color='black',
                            major_tick_line_width=3,
                            major_tick_in=12,
                            location=(0,0))



p.add_layout(color_bar, 'right')
#p.add_layout(color_bar_label, 'right')

r.data_source.selected.on_change('indices',time_dm)

p.title.text ='Single pulse plot'
p.xaxis.axis_label = 'Time'
p.yaxis.axis_label = 'Dispersion measure'

curdoc().add_root(p)

rawdata=sys.argv[1]
#DM_range=sys.argv[2]
#filename=sys.argv[2]


