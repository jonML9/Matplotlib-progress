import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv("UNRATE.csv") #Getting info from the csv file
df['observation_date'] = pd.to_datetime(df['observation_date'])
print(df.size)

plt.plot(df['observation_date'], df['UNRATE']) #Names of tables in the file itself
plt.ylabel('Percentage')
plt.xlabel('Years')
plt.title("USA's Unemployment Rate")
plt.show()

