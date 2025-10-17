import matplotlib.pyplot as plt
import pandas as pd

demography = {
    'category': ['0-9', '10-19', '20-29', '30-39', '40-49', '50-59', '60-69', '70-79', '80+'],
    'percentage': [20.54, 16.35, 17.29, 16.49, 11.75, 9.11, 5.76, 2.07, 0.64]
}


df = pd.DataFrame(demography)

print(df)




plt.barh(df['category'], df['percentage'])
plt.ylabel('Category')
plt.xlabel('Percentage')
plt.title("Uzbekistan's demography")
plt.show()
