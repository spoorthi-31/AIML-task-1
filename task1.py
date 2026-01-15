import pandas as pd

df = pd.read_csv("C:\\Users\\Administrator\\Downloads\\test.csv")
df.head()
df.tail()

df.info()
df.describe()

cat_cols = ['Sex', 'Embarked', 'Pclass']

for col in cat_cols:
    print(col, ":", df[col].unique())
