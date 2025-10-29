import pandas as pd

data = {
    'Size': ['Small', 'Medium', 'Large', 'Medium', 'Small', 'Large'],
    'Color': ['Red', 'Blue', 'Red', 'Green', 'Red', 'Green']
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

def one_hot_encoding (df, columns):
    for col in columns:
        unique_vals = []
        for val in df[col]:
            if val not in unique_vals:
                unique_vals.append(val)

        for category in unique_vals:
            new_col_name = f"{col}_{category}"
            encoded_col = []

            for val in df[col]:
                if val == category:
                    encoded_col.append(1)
                else:
                    encoded_col.append(0)

            df[new_col_name] = encoded_col

        df.drop(columns=[col], inplace=True)

    return df

categorical_columns = ['Size', 'Color']

df = one_hot_encoding(df, categorical_columns)

print("\nDataFrame after One-Hot Encoding:")
print(df)