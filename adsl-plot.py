"""Plots the adsl-log generated log."""
import pandas as pd
import matplotlib.pyplot as plt
# Prepare the data to plot
# set field delimiter and set column names which will also cause reading from row 1
data = pd.read_csv('test.log', sep=';', names=[
                   'datetime', 'severity', 'down', 'up', 'loss', 'server'])
#  we need to filter out ERROR records (with 0 speeds)
indexNames = data[data['severity'] == 'ERROR'].index
data.drop(indexNames, inplace=True)
# convert datetime pandas object to datetime64
data['datetime'] = pd.to_datetime(data['datetime'])
# use a dataframe with just the data I need; cleaner
speeds_df = data[['datetime', 'down', 'up']]

# now plot the graph
fig, ax = plt.subplots()

color = 'tab:red'
speeds_df.plot(ax=ax, x='datetime', y='down', label="DL", linewidth=2, color=color)
ax.set_ylabel('DL', color=color)
ax.tick_params(axis='y', labelcolor=color)

color = 'tab:blue'
ax2 = speeds_df.plot(ax=ax, x='datetime', y='up', secondary_y=True, label="UL", linewidth=2, color=color)
ax2.set_ylabel('UL', color=color)
ax2.tick_params(axis='y', labelcolor=color)

# cannot show a grid since the two scales are different
ax.set_ylim(10, 225)
ax2.set_ylim(15, 50)

color = 'tab:green'
ax.set_xlabel('time', color=color)
ax.tick_params(axis='x', labelcolor=color)

plt.show()
