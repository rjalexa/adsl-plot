"""Plots the adsl-log generated log."""
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates

# set field delimiter and set column names which will also cause reading including row 1; use the datetime as the index
data = pd.read_csv("test.log", sep=';', names=['datetime', 'severity', 'down', 'up', 'loss', 'server'], index_col=0)
data.head()
# convert the dateime string read by read_csv to datetime64
data['datetime'] = pd.to_datetime(data['datetime'])
data.head()
# we will need to discard all ERROR lines (DL:0;UL:0)
indexNames = data[data['severity'] == 'ERROR'].index
data.drop(indexNames, inplace=True)

#  y1 = dl_df.plot(grid=True, label="DL", legend=True, linewidth=5)
#  y2 = ul_df.plot(secondary_y=True, label="UL", legend=True, linewidth=5)
#  y1.set_ylim(180, 215)
#  y2.set_ylim(20, 40)


y1.set_title('Speeds as monitored by adsl-log')
y1.fmt_xdata = mdates.DateFormatter('%Y-%m-%d')
# rotate and align the tick labels so they look better
# fig.autofmt_xdate()

# y1 = ax1.plot(dl_df['datetime'], dl_df['down'], label="DL", linewidth=3)
# y2 = ax1.plot(ul_df['datetime'], ul_df['up'],   label="UL", linewidth=3)
#

plt.show()
