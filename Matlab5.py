import pandas as pd
from matplotlib import pyplot as plt


df = pd.read_csv("UNRATE.csv")

df['observation_date'] = pd.to_datetime(df['observation_date'])

start_date = '1973-03-01'
end_date = '1974-10-31'

filtered_df = df[(df['observation_date'] >= start_date) & (df['observation_date'] <= end_date)]

plt.figure(figsize=(10, 5)) #This line of code should before plt.plot, as it defines the size of the plot
plt.title("USA's Unemployment Rate during Oil Crisis", fontsize=17) #Fontsize after writing the title
plt.plot(filtered_df['observation_date'], filtered_df['UNRATE'])
plt.show()
