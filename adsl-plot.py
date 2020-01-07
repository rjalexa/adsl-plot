"""Plots the adsl-log generated log."""
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates

# set field delimiter and set column names which will also cause reading from row 1
data = pd.read_csv("test.log", sep=';', names=[
                   'datetime', 'severity', 'down', 'up', 'loss', 'server'])
# check type of variables
# data.info()
# convert the dateime string read by read_csv to datetime64
data['datetime'] = pd.to_datetime(data['datetime'])
# select only wanted columns
dl_df = data[['datetime', 'down']]
ul_df = data[['datetime', 'up']]
# check the datetime value is of datetime64 type
# ul_df.info()
fig, ax = plt.subplots()
ax.set_title('Speeds as monitored by adsl-log')

# y1 = dl_df.plot(grid=True, label="DL", legend=True, linewidth=5)
# y2 = up_df.plot(secondary_y=True, label="UL", legend=True, linewidth=5)

# y1.set_ylim(180, 215)
# y2.set_ylim(20, 40)
#  need to fix x axis labels

# rotate and align the tick labels so they look better
fig.autofmt_xdate()

# use a more precise date string for the x axis locations in the toolbar
ax.fmt_xdata = mdates.DateFormatter('%Y-%m-%d')

y1 = ax.plot(dl_df['datetime'], dl_df['down'], label="DL", linewidth=3)
# y2 = ax.plot(dl_df['datetime'], dl_df['up'], label="UL", linewidth=3)

plt.show()
