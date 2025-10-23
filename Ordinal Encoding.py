import pandas as pd

data = {
    'Size': ['Small', 'Medium', 'Large', 'Medium', 'Small', 'Large'],
    'Color': ['Red', 'Blue', 'Red', 'Green', 'Red', 'Green']
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

data = {"Small": 1, "Medium": 2, "Large": 3}
df['Size_Code'] = df['Size'].map(data)

data2 = {"Red": 1, "Blue": 2, "Green": 3}
df['Color_Code'] = df['Color'].map(data2)

print("\nDataFrame after Ordinal Encoding:")
print(df)
