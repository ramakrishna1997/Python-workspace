import pandas as pd
import numpy  as np
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv('USA_Housing.csv')
df=df.head()
print(df)
sns.distplot(df['Price'])
plt.show()
