import streamlit as st


st.set_page_config(
    page_title="Home",
)

st.write("## MELTS-online")


st.markdown(
    """
    ---
    ### Info
    This is a web application to run the thermodynamic software "MELTS" (Ghiorso and Sack 1995, Gualda et al., 2012) online.
    Is utilized the MELTS API (Gleeson and Wieser, in prep) and the web framework application [streamlit](https://streamlit.io/).
    
    
    #### References
    - Ghiorso, M. S., & Sack, R. O. (1995). Chemical mass transfer in magmatic processes IV. A revised and internally consistent thermodynamic model for the interpolation and extrapolation of liquid-solid equilibria in magmatic systems at elevated temperatures and pressures. Contributions to Mineralogy and Petrology, 119, 197-212.
    - Gleeson, M., and Wieser, P.E., (in prep). pyMELTScalc: an open-source Python3 package enabling thermodynamic simulations of magmatic processes.
    - Gualda, G. A., Ghiorso, M. S., Lemons, R. V., & Carley, T. L. (2012). Rhyolite-MELTS: a modified calibration of MELTS 
    optimized for silica-rich, fluid-bearing magmatic systems. Journal of Petrology, 53(5), 875-890. DOI: https://doi.org/10.1093/petrology/egr080
    
    By [Paul Heckmann](https://www.paulheckmann.de/)
"""
)
