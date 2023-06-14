import pandas as pd
import sqlite3 as sl

con = sl.connect('../../nutrition.db')

df = pd.read_csv('nutrients_csvfile.csv')
df.replace("Vegetables A-E", "Vegetables", inplace=True)
df.replace("Vegetables F-P", "Vegetables", inplace=True)
df.replace("Vegetables R-Z", "Vegetables", inplace=True)
df.replace("Fruits A-F", "Fruits", inplace=True)
df.replace("Fruits G-P", "Fruits", inplace=True)
df.replace("Fruits R-Z", "Fruits", inplace=True)


df.to_sql('nutritients', con)


con.close()