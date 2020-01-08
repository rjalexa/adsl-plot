"""Plots the adsl-log generated log."""
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
###### Now prepare the data to plot
# set field delimiter and set column names which will also cause reading including row 1; use the datetime as the index
# data = pd.read_csv("test.log", sep=';', names=['datetime', 'severity', 'down', 'up', 'loss', 'server'], index_col=0)
data = pd.read_csv("test.log", sep=';', names=['datetime', 'severity', 'down', 'up', 'loss', 'server'])
# data.head()
# data.info()
# convert the dateime string read by read_csv to datetime64
data['datetime'] = pd.to_datetime(data['datetime'])
# data.info()
# we will need to discard all ERROR lines (DL:0;UL:0)
indexNames = data[data['severity'] == 'ERROR'].index
data.drop(indexNames, inplace=True)

######
###### Now that data is ready get on with displaying it
######

y1 = data.plot(x='datetime',y='down',grid=True, label="DL", legend=True, linewidth=3)
y2 = data.plot(x='datetime',y='up', secondary_y=True, label="UL", legend=True, linewidth=3)
y1.set_ylim(180, 215)
y2.set_ylim(20, 40)
y1.set_title('Speeds as monitored by adsl-log')
y1.fmt_xdata = mdates.DateFormatter('%Y-%m-%d')
# rotate and align the tick labels so they look better
# fig.autofmt_xdate()

plt.show()
