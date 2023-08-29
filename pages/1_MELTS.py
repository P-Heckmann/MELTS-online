import matplotlib.pyplot as plt

# import PySulfSat as ss
import pyMELTScalc as M

import pandas as pd
import multiprocessing
import streamlit as st

# import Streamlit_app
# import base64
# import os


st.write("## MELTS-online")


def main():
    Model_selected = st.selectbox(
        "Choose MELTS model", ("MELTSv1.0.2", "pMELTS", "MELTSv1.1.0", "MELTSv1.2.0")
    )

    st.markdown("---")

    # file = r"C:\Users\paulh\Desktop\Nucleation\data\Glass_input_example.xlsx"
    # df = ss.import_data(file, suffix="_Liq")
    # sample = df.iloc[0]

    SiO2_Liq = st.number_input("SiO2:", value=50.822, key="SiO2")
    NaO2_Liq = st.number_input("Na2O:", value=2.49, key="Na2O")
    K2O_Liq = st.number_input("K2O:", value=0.247, key="K2O")
    FeOt_Liq = st.number_input("FeOt:", value=13.339, key="FeOt")
    Cr2O3_Liq = st.number_input("Cr2O3:", value=0.04, key="Cr2O3")
    MnO_Liq = st.number_input("MnO:", value=0.252, key="MnO")
    CaO_Liq = st.number_input("CaO:", value=11.356, key="CaO")
    TiO2_Liq = st.number_input("TiO2:", value=2.056, key="TiO2")
    MgO_Liq = st.number_input("MgO:", value=6.631, key="MgO")
    Al2O3_Liq = st.number_input("Al2O3:", value=13.235, key="Al2O3")
    P2O5_Liq = st.number_input("P2O5:", value=0.189, key="P2O5")
    H2O_Liq = st.number_input("H2O:", value=0.1, key="H2O")
    Fe3Fet_Liq = st.number_input("Fe3Fet_Liq:", value=0.1, key="Fe3Fet_Liq")

    sample = {
        "SiO2_Liq": SiO2_Liq,
        "Na2O_Liq": NaO2_Liq,
        "K2O_Liq": K2O_Liq,
        "FeOt_Liq": FeOt_Liq,
        "Cr2O3_Liq": Cr2O3_Liq,
        "MnO_Liq": MnO_Liq,
        "CaO_Liq": CaO_Liq,
        "TiO2_Liq": TiO2_Liq,
        "MgO_Liq": MgO_Liq,
        "Al2O3_Liq": Al2O3_Liq,
        "P2O5_Liq": P2O5_Liq,
    }

    st.markdown("---")

    P = st.number_input("Pressure in bar:", value=1000, key="Pressure")
    deltat_C = st.number_input("dt_C:", value=5, key="dt_C")
    Temp_end_C = st.number_input("Temp_end_C:", value=750, key="Temp_end_C")

    st.markdown("---")

    Fractio_solid = st.checkbox("Frac_solid", value=True)
    if Fractio_solid:
        Frac_solid = True

    Fractio_fluid = st.checkbox("Frac_fluid", value=True)
    if Fractio_fluid:
        Frac_fluid = True

    fin_liquidus = st.checkbox("find_liquidus", value=True)
    if fin_liquidus:
        find_liquidus = True

    st.markdown("---")

    # Add a calculate button
    calculate_button = st.button("Calculate")

    if calculate_button:
        MELTS_FC = M.multi_path(
            Model=Model_selected,
            Fe3Fet_Liq=Fe3Fet_Liq,
            H2O_Liq=H2O_Liq,
            # comp=sample.to_dict(),
            comp=sample,
            Frac_solid=Frac_solid,
            Frac_fluid=Frac_fluid,
            find_liquidus=find_liquidus,
            T_end_C=Temp_end_C,
            dt_C=deltat_C,
            P_bar=P,
        )

        st.write(MELTS_FC)

        # MELTS = MELTS_FC["All"]

        # df = st.dataframe(MELTS)

        # Add a calculate button
        # @st.cache_data
        # def convert_df(df):
        #    # IMPORTANT: Cache the conversion to prevent computation on every rerun
        #    return df.to_csv().encode("utf-8")


#
# csv = convert_df(MELTS)
#
# st.download_button(
#    label="Download data as CSV",
#    data=csv,
#    file_name="MELTS_output.csv",
#    mime="text/csv",
# )


# folder_path = '../'
# files_to_delete = ['Bulk_comp_tbl.txt', 'Liquid_comp_tbl.txt', 'Phase_main_tbl.txt','Solid_comp_tbl','System_main_tbl.txt']

if __name__ == "__main__":
    multiprocessing.freeze_support()  # This line is not necessary for Streamlit apps
    main()
