import pandas as pd

test_file = "data\example_data_spidergram.xlsx"

test_df = pd.read_excel(test_file)

src_file = r"data\Normalization_values.xlsx"
normalization_values = pd.read_excel(src_file, sheet_name="REE_PRIMA_Sun_1995")
normalization_elements = normalization_values.columns

test_df[normalization_elements]

data = []
Normalized_uploaded_df = pd.DataFrame(data)

# Normalize the selected columns by dividing them element-wise
for col in normalization_elements:
    Normalized_uploaded_df[col] = test_df[col] / normalization_values[col].values

# test_df[normalization_elements]

Normalized_uploaded_df
