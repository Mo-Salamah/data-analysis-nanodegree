#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#%%
# city_data = pd.read_csv('city_data.csv')
# city_list = pd.read_csv('city_list.csv')
# global_data = pd.read_csv('global_data.csv')

# %%
# city_global_data = city_data.merge(global_data, on='year')

#%%
# import data
temperature = pd.read_csv("riyadh_temperature.csv")


# %%
# plot the raw trend (no average calculation)
temperature = temperature.query("year >= 1850")
fig, ax = plt.subplots(2,1, sharex=True)
sns.lineplot(x=temperature.year, y=temperature.riyadh_avg_temp, ax=ax[0])
sns.lineplot(x=temperature.year, y=temperature.global_avg_temp, ax=ax[1])


# %%
# calculate running average
running_avg_riyadh = temperature['riyadh_avg_temp'].rolling(window=7).mean()
running_avg_global = temperature['global_avg_temp'].rolling(window=7).mean()


#%%
# plot running average
fig, ax = plt.subplots(2,1, sharex=True)
sns.lineplot(x=temperature.year, y=running_avg_riyadh, ax=ax[0])
sns.lineplot(x=temperature.year, y=running_avg_global, ax=ax[1])
plt.suptitle('Weather Trend in Riyadh and Globally (Celsius)')
# ax[0].set_ylabel("Riyadh Avg. Temperature (C)")
# ax[1].set_ylabel("Global Avg. Temperature (C)")


# %%
