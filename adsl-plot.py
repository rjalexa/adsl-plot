"""Plots the adsl-log generated log."""
import matplotlib.pyplot as plt
# import matplotlib.dates as mdates
import pandas as pd

# set field delimiter and set column names which will also cause reading from row 1
data = pd.read_csv("test.log", sep=';', names=[
                   'datetime', 'severity', 'down', 'up', 'loss', 'server'])

#  we need to filter out ERROR records (with 0 speeds)

speeds_df = data[['datetime', 'down', 'up']]
# speeds_df.info()

y1 = speeds_df.down.plot(grid=True, label="DL", legend=True, linewidth=5)
y2 = speeds_df.up.plot(secondary_y=True, label="UL", legend=True, linewidth=5)
y1.set_ylim(180, 215)
y2.set_ylim(20, 40)
#  need to fix x axis labels
plt.show()
