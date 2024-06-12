import mplcursors
from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
df = pd.read_csv('./fifa_datasets/FIFA23_official_data.csv')

df1 = df[['Name', 'Wage', 'Value']]


def value_to_float(x):
    if type(x) == float or type(x) == int:
        return x
    if 'K' in x:
        if len(x) > 1:
            return float(x.replace('K', '')) * 1000
        return 1000.0
    if 'M' in x:
        if len(x) > 1:
            return float(x.replace('M', '')) * 1000000
        return 1000000.0
    if 'B' in x:
        return float(x.replace('B', '')) * 1000000000
    return 0.0


df1['Wage'] = df['Wage'].replace('[\€]', '', regex=True).apply(value_to_float)
df1['Value'] = df['Value'].replace(
    '[\€]', '', regex=True).apply(value_to_float)
df1['Difference'] = df1['Value'] - df1['Wage']


graph2 = plt.scatter(x='Wage', y='Value', data=df1)

plt.show()
