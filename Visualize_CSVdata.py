import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"Dataset\battles.csv")

fig, axes = plt.subplots(3, figsize=(15,10))
fig.tight_layout(pad=5.0)
#print(df.to_string())
#visualize number of wars fought in each region
region_count = df.region.value_counts().plot(ax = axes[0],kind='bar')
region_count.set_xlabel("Region")
region_count.set_ylabel("Number of Wars fought")
axes[0].set_title('A')
#visualize number of wars fought in each location
location_count = df.location.value_counts().plot(ax = axes[1],kind="bar")
location_count.set_xlabel("Location")
location_count.set_ylabel("Number of Wars fought")
axes[1].set_title('B')
#visualize number of wars fought in a year
year_count = df.year.value_counts().plot(ax = axes[2],kind="bar")
year_count.set_xlabel("Year")
year_count.set_ylabel("Number of Wars fought")
axes[2].set_title('C')
plt.subplot_tool()
plt.show()

