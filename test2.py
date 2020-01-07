"""Plots the adsl-log log."""
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# set field delimiter and set column names which will also cause reading from row 1
data = pd.read_csv("test.log", sep=';', names=['datetime', 'severity', 'down', 'up', 'loss', 'server'])
data.head()
dl_df = data[['datetime', 'down']]
ul_df = data[['datetime', 'up']]

dl_df.plot()
plt.show()
