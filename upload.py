import pandas
df = pandas.read_excel("RAW_DATA.xlsx")

print(df['Time'].values[1])
