import streamlit as st
from streamlit.components.v1 import html

def show_charging_trends():
    st.header("EV Charging Trends in Germany")

    # --- Section 1: Charging Point Distribution & Growth Overview ---
    st.subheader("Charging Point Distribution & Infrastructure Growth")

    st.markdown("""
    ### Chart 1: Distribution of AC vs. DC Charging Points  
    - This map compares **fast (DC)** and **normal (AC)** EV charging points across Germany.  
    - **Urban areas** show a **higher density of AC chargers**, aligning with city dwellers’ charging behavior.  
    - **Northeast Germany** stands out with a **notable shortage of DC fast chargers**.  
    - **Overall**, **AC charging points are significantly more common** than DC fast chargers throughout the country.
    """)

    # Embed Chart 1
    dashboard_1 = """
    <div style="width:100%; height:1600px;">
        <iframe 
            src="https://public.tableau.com/views/workbooktest_17453371908520/EVChargingDataGermany?:embed=y&:display_count=yes&:showVizHome=no" 
            width="100%" 
            height="100%" 
            frameborder="0" 
            style="border:none;">
        </iframe>
    </div>
    """
    html(dashboard_1, height=1200)

    st.markdown("""
    ### Chart 2: Growth of Charging Infrastructure (2020–2023)  
    - From **2020 to 2023**, there was a **substantial increase** in the number of charging stations—almost doubling in size.  
    - This expansion aligns with Germany’s goal of creating a **robust and accessible EV charging network** by **2030**.
    """)

    st.markdown("---")

    # --- Section 2: Charging Cost Trends ---
    st.subheader("EV Charging Cost Trends (2022–2025)")

    st.markdown("""
    - EV charging is categorized into **Standard**, **Fast**, and **Ultra-Fast** tiers.  
    <br>
    <b>2022</b> — <b>Charging costs rose sharply</b>, driven by the <b>energy crisis</b>, <b>record-high electricity prices</b>, and a <b>surge in EV usage</b>.  
    <br>
    <b>2023</b> — <b>Prices dropped</b>, thanks to <b>electricity market stabilization</b>, <b>provider competition</b>, and <b>subscription model adoption</b>.  
    <br>
    <b>2024</b> — Costs <b>rose again</b> due to the <b>removal of subsidies</b>, increased <b>roaming fees</b>, and <b>higher energy/infrastructure expenses</b>.  
    <br>
    <b>2025 Outlook</b>  
    - Expect <b>moderate increases</b> in cost, with more <b>price variability</b> based on <b>time of day</b> and <b>charging location</b>.  
    - Subscription models will continue to help <b>users manage and predict their charging expenses</b>.
    """, unsafe_allow_html=True)

    # Embed Chart 2
    dashboard_2 = """
    <div style="width:100%; height:800px;">
        <iframe 
            src="https://public.tableau.com/views/EVChargingpricesinGermany2024/Chargingstationprices20-24?:embed=y&:display_count=yes&:showVizHome=no" 
            width="100%" 
            height="100%" 
            frameborder="0" 
            style="border:none;">
        </iframe>
    </div>
    """
    html(dashboard_2, height=800)

    st.markdown("---")

    
    # --- Final Notes ---
    st.markdown("""
    ### Conclusion  
    Germany is making **steady progress** in building out its EV charging network.  
    However, **regional disparities** and **fluctuating pricing trends** pose ongoing challenges.  
    Continued **investment, innovation**, and **policy support** are key to a reliable and accessible charging future.
    """)

# Example usage
# show_charging_trends()
