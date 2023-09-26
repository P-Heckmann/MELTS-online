import pyMELTScalc as M
import multiprocessing
import os

# import sys

# sys.path.append("../package")


def main():
    Model_selected = "MELTSv1.2.0"
    SiO2_Liq = 50.822
    NaO2_Liq = 2.49
    K2O_Liq = 0.24
    FeOt_Liq = 13.339
    Cr2O3_Liq = 0.04
    MnO_Liq = 0.25
    CaO_Liq = 11.35
    TiO2_Liq = 2.056
    MgO_Liq = 6.63
    Al2O3_Liq = 13.2
    P2O5_Liq = 0.189
    H2O_Liq = 0.1
    Fe3Fet_Liq = value = 0.1

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

    P = 1000
    deltat_C = 5
    Temp_end_C = 750
    Fractio_solid = True
    Fractio_fluid = True
    fin_liquidus = True

    MELTS_FC = M.multi_path(
        Model=Model_selected,
        Fe3Fet_Liq=Fe3Fet_Liq,
        H2O_Liq=H2O_Liq,
        comp=sample,
        Frac_solid=Fractio_solid,
        Frac_fluid=Fractio_fluid,
        find_liquidus=fin_liquidus,
        T_end_C=Temp_end_C,
        dt_C=deltat_C,
        P_bar=P,
    )

    print(MELTS_FC)

    # Specify the folder path where the files are located
    folder_path = ""

    # List of files to delete
    files_to_delete = [
        "Bulk_comp_tbl.txt",
        "Liquid_comp_tbl.txt",
        "Phase_main_tbl.txt",
        "Solid_comp_tbl.txt",
        "System_main_tbl.txt",
        "liquid-model-batch.inp",
    ]

    # Iterate through the list of files and delete them
    for file_name in files_to_delete:
        # Construct the full path to the file
        file_path = os.path.join(folder_path, file_name)

        # Check if the file exists before attempting to delete it
        if os.path.exists(file_path):
            # Delete the file
            os.remove(file_path)
            print(f"Deleted {file_name}")
        else:
            print(f"{file_name} not found")


if __name__ == "__main__":
    multiprocessing.freeze_support()  # This line is not necessary for Streamlit apps
    main()
