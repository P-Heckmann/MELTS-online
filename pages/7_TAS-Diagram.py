import pandas as pd
import streamlit as st
from Functions import Create_TAS_Plot


st.write("## Total Alkali vs Silica plot")


st.markdown(
    """
    ---
    ### How to create your plot:
    
    1) Checkout the example file serving as a template.
    2) Upload your own file.
    3) Download the plot as an image.
    
    ### Info
    
    Pyrolite by Williams et al., 2020
    
    Example data by Wörner et al., 2000
    
    - Williams, M. J., Schoneveld, L., Mao, Y., Klump, J., Gosses, J., Dalton, H., ... & Barnes, S. (2020). Pyrolite: Python for geochemistry. Journal of Open Source Software, 5(50), 2314.
    - Wörner, G., Lezaun, J., Beck, A., Heber, V., Lucassen, F., Zinngrebe, E., Rössling, R., and Wilke, H. G., 2000, Precambrian and Early Paleozoic evolution of the Andean basement at Belén (northern Chile) and Cerro Uyarani (western Bolivia Altiplano): Journal of South America Earth Science Review, v. 13, p. 717-737.
    ---
"""
)


st.write("### Example plot")

example_file = "data\example_data_tas.xlsx"
example_image = "data\example_tas.png"

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

            image_buffer = Create_TAS_Plot(uploaded_df)
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
