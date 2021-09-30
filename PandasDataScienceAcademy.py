import pandas as pd
import matplotlib.pyplot as plt

file_name = "arquivos/salarios.csv"
df = pd.read_csv(file_name)
print(df.head())


file_name = "arquivos/binary.csv"
df2 = pd.read_csv(file_name)
print(df2.head())
