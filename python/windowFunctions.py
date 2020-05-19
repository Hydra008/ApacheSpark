import pandas as pd
import numpy as np

# Rolling
df = pd.DataFrame(np.random.randn(10, 4),
   index = pd.date_range('1/1/2000', periods=10),
   columns = ['A', 'B', 'C', 'D'])
print(df)
print (df.rolling(window=3).mean())

# Expanding
df.expanding(min_periods=3).mean()
