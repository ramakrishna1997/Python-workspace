import pandas as pd
import pivottablejs
from pivottablejs import pivot_ui
import matplotlib.pyplot as plt
df=pd.read_csv("C:/Users/Ramakrishna/Desktop/Clean superstore.csv")
# print(df)
pivot_ui(df.head(20))
