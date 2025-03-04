import pandas as pd

df = pd.read_excel("RAW_DATA.xlsx")

print("Original column names:", df.columns.tolist())

df.columns = df.columns.str.strip()
df.rename(columns={"PJM DA LMP": "max_price", "PJM RT LMP": "min_price"}, inplace=True)

# Drop rows with NaN values in 'max_price' or 'min_price'
df.dropna(subset=["max_price", "min_price"], inplace=True)

time_series_data = df[["max_price", "min_price"]].values


print("Updated column names:", df.columns.tolist())
print("First 5 rows of the DataFrame:")
print(df.head())


