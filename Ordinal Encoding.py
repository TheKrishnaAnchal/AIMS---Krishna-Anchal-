import pandas as pd

data = {
    'Size': ['Small', 'Medium', 'Large', 'Medium', 'Small', 'Large'],
    'Color': ['Red', 'Blue', 'Red', 'Green', 'Red', 'Green']
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

def ordinal_encode_loop(df, columns, sort_values=False):
    encoded_df = df.copy()
    mappings = {}

    for col in columns:

        unique_vals = list(set(encoded_df[col]))
        if sort_values:
            unique_vals.sort()

        mapping = {}
        for i in range(len(unique_vals)):
            mapping[unique_vals[i]] = i + 1

        mappings[col] = mapping

        encoded_col = []
        for val in encoded_df[col]:
            encoded_col.append(mapping[val])
        encoded_df[col + '_Code'] = encoded_col

    return encoded_df, mappings

categorical_columns = ['Size', 'Color']
encoded_df, encoding_maps = ordinal_encode_loop(df, categorical_columns, sort_values=True)

print("\nDataFrame after Ordinal Encoding:")
print(encoded_df)

print("\nEncoding Maps:")
for col, mapping in encoding_maps.items():
    print(f"{col}: {mapping}")
