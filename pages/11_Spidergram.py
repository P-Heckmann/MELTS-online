import streamlit as st
import pandas as pd
from Functions import Spidergram_Normalization, Create_Spidergram


st.write("## Spidergram")


st.markdown(
    """
    ---
    ### How to create your plot:
    
    1) Checkout the example file serving as a template.
    2) Upload your own file.
    3) Download the plot as an image.
    
    ### Info
    
    ---
"""
)


st.write("### Example plot")

example_file = "data\example_data_spidergram.xlsx"
example_image = "data\example_spidergram.png"

st.image(
    example_image,
    caption=None,
    width=None,
    use_column_width=None,
    clamp=False,
    channels="RGB",
    output_format="auto",
)
# Download Example excel file
with open(example_file, "rb") as template_file:
    template_byte = template_file.read()

st.download_button(
    label="Click to Download Example File",
    data=template_byte,
    file_name="example_data.xlsx",
    mime="application/octet-stream",
)


st.markdown("---")


normalization_reference = st.selectbox(
    "Choose a normalization reference",
    (
        "MORB_Pearce_1983",
        "MORB_Pearce_1996",
        "OIB_Sun_1989",
        "PRIMA_Long_Sun_1995",
        "PRIMO_Wood_1979",
        "REE_Chondrite_Nakamura_1974",
        "EMORB_Sun_McDonough_1989",
        "NMORB_Long_Sun_McDonough_1989",
        "PRIMA_Long_Sun_McDonough_1989",
        "REE_PRIMA_Sun_1995",
        "REE_Chondrite_Boynton_1984",
        "Bevins_1984",
    ),
)


def main():
    st.write("### Excel/CSV Upload and Plot")

    uploaded_file = st.file_uploader("Upload Excel or CSV file", type=["xlsx", "csv"])

    if uploaded_file is not None:
        try:
            uploaded_df = (
                pd.read_excel(uploaded_file)
                if uploaded_file.name.endswith(".xlsx")
                else pd.read_csv(uploaded_file)
            )

            Normalized_uploaded_df = Spidergram_Normalization(
                uploaded_df, normalization_reference
            )

            # st.write("Normalized DataFrame:")
            # st.dataframe(Normalized_uploaded_df)

            image_buffer = Create_Spidergram(
                Normalized_uploaded_df, normalization_reference
            )
            st.image(image_buffer, caption="", width=800)  # Adjust width as needed

            st.download_button(
                label="Download diagram",
                data=image_buffer,
                file_name="generated_image.png",
                mime="image/png",
            )

        except Exception as e:
            st.error(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
