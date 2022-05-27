import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.random(size=(5, 3)))
print("Sample dataframe taken is :")
print(df)
print("The dataframe obtained after subtacting mean is given below : ")
df=df.sub(df.mean(axis=1), axis=0)
print(df)