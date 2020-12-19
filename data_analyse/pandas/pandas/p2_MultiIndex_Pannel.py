import numpy as np
import pandas as pd

df = pd.DataFrame(dict(month=[1, 4, 7, 10], year=[2012, 2014, 2012, 2013], sale=[55, 40, 84, 31]))
df = df.set_index(['month', 'year'])
print(df)
print(df.index.names)
print(df.index.levels)
# Panel 已被弃用
