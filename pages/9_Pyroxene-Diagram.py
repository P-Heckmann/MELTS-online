import streamlit as st
import pandas as pd
from Functions import Create_Pyroxene_Plot

st.write("## Plagioclase")


st.markdown(
    """
    ---
    ### Info
    
    ---
"""
)


st.write("### Example plot")

example_file = "data\example_data_pyroxene.xlsx"
example_image = "data\example_pyroxene.png"

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
            st.write("Uploaded DataFrame:")
            st.dataframe(uploaded_df)

            image_buffer = Create_Pyroxene_Plot(uploaded_df)
            st.image(image_buffer, caption="", width=800)  # Adjust width as needed

            if st.button("Download Image"):
                st.download_button(
                    "Download Image",
                    data=image_buffer,
                    file_name="generated_image.png",
                    key="download",
                )
        except Exception as e:
            st.error(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
