# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import pandas as pd
import numpy as np
import matplotlib
print matplotlib.get_backend()
matplotlib.use('qt4agg')
print matplotlib.get_backend()
import matplotlib.pyplot as plt

# <codecell>

########################################################
#Plot appliance traces against background noise traces
########################################################

##GLOBALS
#Path to FFT_averaged data stored as CSVs
dirpath='C:\Users\GEETALI\Desktop\\'
#Location of Book.csv containing metadata of traces
bookpath='C:\Users\GEETALI\Desktop\\Book1.csv'
#Index of first trace to be plotted in Book.csv
x=8
#Index of second trace tobe plotted in Book.csv
y=9

x=x-2
y=y-2

# <codecell>

#Read Book.csv data
df = pd.read_csv(bookpath)

#Stores appliances' names in names array
names=df['Appliances'].tolist()

#Stores traces' names (e.g. Trace_xxxx) in names array
traces=df['Traces'].tolist()

# <codecell>

path1 = dirpath+traces[x]+'_FFT_Averaged'
path2 = dirpath+traces[y]+'_FFT_Averaged'

#Read data from both FFT_Averaged CSVs to dataframes DF1 and DF2
DF1 = pd.read_csv(path1+'.csv',header=None, names = ['Frequency','Data'])
DF2 = pd.read_csv(path2+'.csv',header=None, names = ['Frequency','Data'])

# <codecell>

#Print trace numbers and appliance names of traces to be plotted
print traces[x],traces[y]
print names[x],names[y]

# <codecell>


ax = plt.gca();
ax.grid(True); #Create grid in plot

plt.plot(DF1['Frequency'],DF1['Data'],'b') #Plot first trace in blue
plt.plot(DF2['Frequency'],DF2['Data'],'r') #Plot second trace in red

plt.locator_params(axis = 'x', nbins = 10)
plt.xlabel("Frequency ( in Khz )"); #Label x_axis
plt.ylabel("Amplitude ( in dBm )"); #Label y_axis
plt.ylim((-150, -10)) #Set x_axis limits
plt.xlim((10,1000)) #Set y_axis limits

plt.legend([names[x],names[y]]);  #Generate legend for plots

plt.xticks(rotation=70) #Rotate x_axis values by 70 degrees

mng = plt.get_current_fig_manager()
mng.window.showMaximized() #Maximize plot window

#Save plot to a Plots directory within current directory
plt.savefig(dirpath+"Plots\\"+str(names[y])+"_"+str(names[x])+"_USRP.png");

#Display plot
plt.show();

# <codecell>

    

# <codecell>


