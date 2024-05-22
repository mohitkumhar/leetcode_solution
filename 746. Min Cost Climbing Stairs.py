import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = sns.load_dataset('tips').head(20)

# print(data.to_string())

sns.catplot(x='tip', y='size', data=data)



