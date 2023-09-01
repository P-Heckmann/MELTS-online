import streamlit as st


st.set_page_config(
    page_title="Home",
)

st.write("## Petrology-online")


st.markdown(
    """
    ---
    ### Info
    This is a petroloy website that uses recent python libaries ...
    
    Compilation by [Paul Heckmann](https://www.paulheckmann.de/)
    
    ---
    ####  Petrology related python libraries used:
    
    - PyMELTScalc (Gleeson and Wieser, in prep) 
    - Pyrolite (Williams et al., 2020) https://pyrolite.readthedocs.io/en/main/
    - Thermobar (Wieser et al,. 2022) https://thermobar.readthedocs.io/en/latest/Examples/Five_min_intro.html
    - PySulfSat (Wieser & Gleeson, 2022) https://pysulfsat.readthedocs.io/en/latest/
    
    
    ---
    #### General python libraries used:

    - [streamlit](https://streamlit.io/) for the web framework
    - [ternary] (https://pypi.org/project/ternary/)
    - [mplstereonet] (https://mplstereonet.readthedocs.io/en/latest/mplstereonet.html)

    ---
    The thermodynamic calculations are based on rhyolite-MELTS (Ghiorso and Sack 1995, Gualda et al., 2012)
    
    #### References
    - Ghiorso, M. S., & Sack, R. O. (1995). Chemical mass transfer in magmatic processes IV. A revised and internally consistent thermodynamic model for the interpolation and extrapolation of liquid-solid equilibria in magmatic systems at elevated temperatures and pressures. Contributions to Mineralogy and Petrology, 119, 197-212. DOI: https://doi.org/10.1007/BF00307281
    - Williams, Morgan J and Schoneveld, Louise and Mao, Yajing and Klump, Jens and Gosses, Justin and Dalton, Hayden and Bath, Adam and Barnes, Steve (2020). Pyrolite: Python for geochemistry. Journal of Open Source Software, 5(50), 2314. DOI: https://doi.org/10.21105/joss.02314
    - Gleeson, M., and Wieser, P.E., (in prep). pyMELTScalc: an open-source Python3 package enabling thermodynamic simulations of magmatic processes. DOI:
    - Gualda, G. A., Ghiorso, M. S., Lemons, R. V., & Carley, T. L. (2012). Rhyolite-MELTS: a modified calibration of MELTS.  DOI: https://doi.org/10.1093/petrology/egr080
    optimized for silica-rich, fluid-bearing magmatic systems. Journal of Petrology, 53(5), 875-890. DOI: https://doi.org/10.1093/petrology/egr080
    - Wieser, P., Petrelli, M., Lubbers, J., Wieser, E., Özaydin, S., Kent, A. J., & Till, C. (2022). Thermobar: an open-source Python3 tool for thermobarometry and hygrometry. DOI: https://doi.org/10.31223/X5FD0K
    - Wieser, P., & Gleeson, M. (2022). PySulfSat: An Open-Source Python3 Tool for modelling sulfide and sulfate saturation. DOI:
"""
)
