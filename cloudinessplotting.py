import pandas as pd
import json
import os
from fnmatch import fnmatch
import matplotlib.pyplot as plt

basepath = '/Users/paulclanon/Documents/Jupyter/cloudiness/'
# read json, make dict, :
first_month = 'cloudiness202103.json'
months = [name for name in os.listdir(basepath) if fnmatch(name, '*.json')]

with open(f'/Users/paulclanon/Documents/Jupyter/cloudiness/{first_month}', 'r') as openfile:
    
        cloudiness_month = json.load(openfile)

df = pd.DataFrame(list(cloudiness_month.items()), columns=['Date', 'Cloudiness'])
df['Date'] = pd.to_datetime(df['Date'])

other_months = ['cloudiness202104.json', 'cloudiness202105.json', 'cloudiness202106.json', 
                'cloudiness202107.json','cloudiness202108.json']


for a in range(len(other_months)):

    with open(f'{basepath}{other_months[a]}', 'r') as openfile:
    
        cloudiness_month = json.load(openfile)
        df_by_month = pd.DataFrame(list(cloudiness_month.items()), columns=['Date', 'Cloudiness'])
        df_by_month['Date'] = pd.to_datetime(df_by_month['Date'])
        df = pd.concat([df, df_by_month], ignore_index=False)
    

   
df.sort_values(by='Date', inplace=True, ascending=True)
# df.describe()
# df.head(60)    

# then plot
fig=plt.figure()
ax=fig.add_subplot()
ax.set_ylabel('Avg Grayscale', fontsize=16)
ax.set_xlabel('Month', fontsize=14)
df.plot(kind='line', x='Date', y='Cloudiness', linewidth=1, color='b', ax=ax)

fig.savefig('/Users/paulclanon/Downloads/cloudiness.png', dpi=300)
