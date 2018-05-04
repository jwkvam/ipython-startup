import numpy as np
import numpy.random as rng
import pandas as pd
import pendulum
import os
try:
    import joblib
except ImportError:
    print('joblib not installed')
    pass
try:
    import matplotlib as mpl
    if 'DISPLAY' not in os.environ:
        mpl.use('Agg')
    import matplotlib.pyplot as plt
    import seaborn as sns
    sns.set()
    sns.set_style('whitegrid')
except ImportError:
    print('matplotlib or seaborn not installed')
    pass
from scipy import linalg as LA
from glob import glob

def figsize(sizex, sizey):
    mpl.rcParams['figure.figsize'] = (sizex, sizey)

# text display width
pd.options.display.width = 100
