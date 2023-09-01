import streamlit as st
import pandas as pd
from pyrolite.mineral.mindb import get_mineral
from pyrolite.mineral.normative import endmember_decompose
import pandas as pd


st.write("## Mineral endmembers")


st.markdown(
    """
    ---
    ### How to get the endmember compositions
    
    1) Checkout the example file 
    
    ### Info
    
    ---
"""
)

selected_mineral = st.selectbox(
    "Select a mineral",
    (
        "spinel",
        "amphibole",
        "olivine",
        "garnet",
        "epidote",
        "pyroxene",
        "mica",
        "feldspar",
    ),
)


st.write("### Example output")


example_file = "data\example_data_endmembers.xlsx"

df = pd.read_excel(example_file)

df.set_index("sample", inplace=True)
df
df = df.T
df.reset_index(inplace=True)

element_value_dict = df.set_index("index")["sample1"].to_dict()

# comp = pd.Series({"MgO": 42.06, "SiO2": 39.19, "FeO": 18.75})
# data = {"Element": ["MgO", "SiO2", "FeO"], "Value": [42.06, 39.19, 18.75]}
# df = pd.DataFrame(data)


# Convert the "Value" column of the DataFrame to a Series
# element_value_dict = df.set_index("Element")["Value"].to_dict()
comp_new = pd.Series(element_value_dict)

ed = endmember_decompose(pd.DataFrame(comp_new).T, endmembers="olivine", molecular=True)
ed
