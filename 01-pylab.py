from __future__ import division, print_function
import numpy as np
import numpy.random as rng
import pandas as pd
import os
import joblib
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import linalg as LA
from glob import glob

def figsize(sizex, sizey):
    mpl.rcParams['figure.figsize'] = (sizex, sizey)

# text display width
pd.options.display.width = 100
