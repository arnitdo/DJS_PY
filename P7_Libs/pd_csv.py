import pandas

df = pandas.read_csv('data.csv')

print(df)
print('-' * 20)
print(df.shape)
print('-' * 20)
print(df.iloc[1])
print('-' * 20)
print(df.loc[1])
print('-' * 20)
print(df.loc[[0]])