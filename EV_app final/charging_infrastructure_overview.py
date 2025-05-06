import streamlit as st
from streamlit.components.v1 import html

def show_charging_infrastructure_overview():
    st.header("Charging Infrastructure Overview in Germany")

    # Description of the visualization
    st.write("""
    This visualization provides insights into the trends in EV charging infrastructure in Germany.
    It includes data on the number of charging stations, types of chargers, and their distribution across different regions.
    """)

    # First set of key observations
    
    st.markdown("""
                

            
    ## **Chart 1: Fuel Stations vs. EV Charging Points**  
    - **Fuel stations continue to outnumber EV charging points** across Germany.  
    - **Infrastructure density** is notably higher in **South** and **West Germany**, where the network of charging stations is more developed.  
    - **Northeast Germany** has a **significant gap** in both fuel and EV charging infrastructure.  
    - **Berlin** stands out with a **relatively high density of charging points**, reflecting its role as a key EV hub.  
    - **Key Insight:** Germany’s EV charging infrastructure still has a **long way to go** to catch up with the more established fuel station network.
    """)

    # Embed the first Tableau visualization
    tableau_html_1 = """
    <iframe src="https://public.tableau.com/views/EVChargingandGasStationInfrastructureinGermany2024/EVChargingandGasStationsInfrastractureinGer024?:embed=y&:display_count=yes&:showVizHome=no" 
            width="100%" height="1000" frameborder="0" style="border:none;">
    </iframe>
    """
    html(tableau_html_1, height=1000)

    # Second set of key observations
    st.subheader("Top Cities with Most EV Charging Points")
    st.markdown("""
    - **Berlin** leads the country with **2,209 charging points**, closely followed by **Munich** with **2,168**.  
    - Larger cities show higher demand for EV charging stations, driven by their larger population and investment in EV infrastructure.  
    - Significant expansion in charging infrastructure is expected by **2030**, particularly in **Berlin**, where a **planned growth** will enhance its position as an EV charging hub.
    """)

    # Embed the second Tableau visualization
    tableau_html_2 = """
    <iframe src="https://public.tableau.com/views/Top10Citieswithchargingpointsingermany/Top10CitiesWithChargingPoints?:language=en-US&:display_count=n&:origin=viz_share_link&:embed=yes&:showVizHome=no" 
            width="100%" height="300" frameborder="0" style="border:none;">
    </iframe>
    """
    html(tableau_html_2, height=300)

    # Final key takeaways
    st.markdown("""
    ### **Key Takeaways:**  
    - Germany's **EV charging infrastructure** is growing but still lags behind the fuel station network.  
    - The **Southern and Western regions** are better served, while **Northeast Germany** and smaller towns need more investment.  
    - **Berlin** is leading the charge, both in terms of the number of charging points and planned infrastructure investments by **2030**.
    """)

# To display the overview, just call the function:
# show_charging_infrastructure_overview()
