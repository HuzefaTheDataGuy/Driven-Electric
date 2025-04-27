import streamlit as st
from streamlit.components.v1 import html

def show_ev_segment_evolution():
    st.header("EV Adoption Trends by Vehicle Type over Time")

    
    # Tableau embed code optimized for Streamlit
    tableau_embed_code = """
    <div style="width:100%; height:800px;">
    <iframe 
        src="https://public.tableau.com/views/BEVModes-Germany2024/BEVModesOverTimeGermany?:embed=y&:display_count=yes&:showVizHome=no"
        width="100%" 
        height="100%"
        frameborder="0"
        style="border:none">
    </iframe>
    </div>
    """
    st.markdown("""
    - The dataset used for this analysis highlights adoption trends across different **EV vehicle types**.
    - A **significant increase** in EV **car** purchases began in **2019**, marking a clear turning point in consumer adoption.
    - **EV vans** followed with **moderate growth**, showing steady but less dramatic uptake.
    - **EV trucks and buses** saw **only slight increases**, indicating slower adoption in commercial and public transport sectors.
    """)
    
    # Display in Streamlit with responsive sizing
    html(tableau_embed_code, height=800)

# Usage in your app:
# show_tableau_viz()