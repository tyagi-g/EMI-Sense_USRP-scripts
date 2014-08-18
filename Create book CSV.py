# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import numpy as np
from scipy import fft, arange,signal
import scipy 
import pandas as pd
from os import listdir
from os.path import isfile,join

# <codecell>

##############################################
#Generate a list of all USRP traces as a CSV
##############################################


###GLOBALS
#Path to directory where USRP data dump files of type "Trace_xxxx" are stored
dirpath='C:\Users\GEETALI\Desktop\\02-07-14'
#Path to directory where book.csv should be created
bookpath='C:\Users\Example\Desktop'


# <codecell>

#Generate list of filenames
files=[f for f in listdir(dirpath) if (isfile(join(dirpath,f)) and f.startswith("Trace_")) and (not(f.endswith(".csv")))]

#Initialize pandas dataframe
df=[]
df = pd.DataFrame(columns=['Traces','Appliances'], index=range(len(files)), dtype=float)
df['Traces']=files

#Create CSV from dataframe
df.to_csv(bookpath+"\Book.csv",index=False,index_label=False)

