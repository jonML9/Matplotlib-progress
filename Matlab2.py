import matplotlib.pyplot as plt
import pandas as pd

sales = {
    'years': [2020, 2021, 2022, 2023, 2024],
    'export': [14.56, 16.48, 21.92, 24.07, 26.94]
}

df = pd.DataFrame(sales)

plt.pie(df['export'], labels=df['years'], autopct='%1.1f%%') #'labels' for creating those pieces of the pie and autopct for showing the percentage of each piece
plt.title('Export for 5 years') #Title
plt.show()