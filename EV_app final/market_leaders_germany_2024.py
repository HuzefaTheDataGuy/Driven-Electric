import streamlit as st
from streamlit.components.v1 import html
from PIL import Image
import base64
from io import BytesIO
import os


def show_market_leaders_germany_2024():
    # Header for the Streamlit app
    st.header("BEV Market Leaders in Germany - 2024")

    # Description of the visualization
    st.write("""
    In this section, we will explore the market leaders in the fully electric vehicles (BEV) segment in Germany for 2024.
    The visualizations will provide insights into the top brands and their BEV sales. Additionally, we will discuss model range per top 5 brands according to customer preferences.
    """)

    # ===================== FIRST VISUALIZATION =====================
    st.subheader("Top 20 BEV Brands in Germany 2024")
    # Embed Tableau dashboard using iframe
    
    st.components.v1.html(
        f"""
        <div style="width:100%; height:650px; margin-bottom: 400px;">
            <iframe 
                src="https://public.tableau.com/views/Top20BEVBrandsinGermany/BEVnon-BEVSales2024inGermany?:showVizHome=no&:embed=true"
                width="100%" 
                height="100%"
                frameborder="0"
                allowfullscreen
                style="border:none;">
            </iframe>
        </div>
        """, height=650
    )
    
    st.markdown("""
    In 2024, the top 20 BEV manufacturers led the German market, with **Volkswagen (62,108 units)**, 
    **BMW (42,066)**, **Tesla (37,574)**, **Mercedes (33,991)**, and **Škoda (25,308)** making up the top 5.
    
    <div style="width:100%; height:650px; margin: 80px 0;">
        <iframe 
            src="https://public.tableau.com/views/BEVModes-Germany2024/TopBEVBrandsinGermany2024?:embed=y&:display_count=yes&:showVizHome=no" 
            width="100%" 
            height="100%" 
            frameborder="0" 
            style="border:none;" 
            allowfullscreen>
        </iframe>
    </div>

    Volkswagen dominated both the German and broader European markets, reinforcing its strong position. 
    German brands overall performed well, likely due to their long-standing reputation for quality and reliability, 
    despite the growing presence of affordable and increasingly competitive Chinese EVs.

    Tesla, the only non-European brand in the top 5, ranked third. With **100% BEV sales**, Tesla’s strong global 
    reputation and leadership in electric mobility likely contributed to its popularity. Notably, the **Tesla Model Y** 
    has been the best-selling EV in Germany and globally over the past three years.
    """, unsafe_allow_html=True
    )

    st.divider()

    # ===================== SECOND VISUALIZATION =====================
    st.subheader("Most popular BEV Models in Germany 2024")
    
    # Fixed and optimized embed code for second visualization
    viz2_url = (
        "https://public.tableau.com/views/BEVModelsinGermany/BEVModelsinGermany"
        "?:embed=y"
        "&:showVizHome=no"
        "&:toolbar=yes"
        "&:display_count=no"
        "&:language=en-US"
    )
    
    st.components.v1.html(
        f"""
        <div style="width:100%; height:800px;">
            <iframe 
                src="{viz2_url}"
                width="100%" 
                height="100%"
                frameborder="0"
                allowfullscreen
                style="border:none;">
            </iframe>
        </div>
        """, height=800
    )

    st.header("BEV Models per Brand & Top Sellers")
    
    st.markdown("""
    **Key Insights:**
    - Shows model diversity across brands
    - Identifies market leaders by product offerings
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Top 3 Brands by Models")
        st.markdown("""
        1. **Mercedes**: 37 models  
        2. **Porsche**: 18 models  
        3. **Opel/Peugeot/Citroën**: 15 models each (tie)
        """)
    
    with col2:
        st.subheader("Top Selling Models (2024)")
        st.markdown("""
        | Model | Units Sold |  
        |-------|-----------|
        | Tesla Model Y | 29,896 |  
        | Škoda Enyaq | 25,262 |  
        | VW ID.4 & ID.5 | 31,611 (combined) |
        
        *Tesla Model Y: Best-seller for 3 consecutive years*
        """)





    # Load the image
    
    tesla_y = Image.open('./images/tesla_y.png')

    # Convert image to base64
    buffered = BytesIO()
    tesla_y.save(buffered, format="PNG")
    img_b64 = base64.b64encode(buffered.getvalue()).decode()

    # Display image in the center using HTML
    st.markdown(
        f"""
        <div style="display: flex; justify-content: center; align-items: center;">
            <img src="data:image/png;base64,{img_b64}" style="width:100%; max-width:400px;">
        </div>
        """,
        unsafe_allow_html=True
    )

    # Spacer
    st.markdown("<br>", unsafe_allow_html=True)    
    
    st.divider()






    
    # ===== Chart 2: Price vs Range =====
    st.header("Price vs Range Analysis")
    
    st.markdown("""
    **Key Findings:**
    - Higher price generally means more range
    - Notable price-range benchmarks in the market
    """)
    
    st.markdown("""
    **Standout Examples:**
    - **Tesla Model Y**  
      • Range: 700 km  
      • Price: €95,134  
      • Benchmark for premium segment
    
    - **VW Group Vehicles**  
      • Consistent range: 350-500 km  
      • Suggests shared battery technology  
      • Popular mid-range choice
    """)
    
    st.warning("Consumer Insight: Many buyers opt for cheaper models with comparable range to premium alternatives.")
    
    st.divider()
    
    # ===== Chart 3: Battery Efficiency =====
    st.header("Battery Efficiency Comparison")
    
    st.markdown("""
    **Key Relationships:**
    - Battery size vs achievable range
    - Efficiency differences between manufacturers
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric("Tesla Model Y Efficiency", "9.33 km/kWh")
        st.markdown("""
        - Battery: 75 kWh  
        - Range: 700 km  
        - Optimal efficiency
        """)
    
    with col2:
        st.metric("Lucid Air Efficiency", "6.47 km/kWh") 
        st.markdown("""
        - Battery: 112 kWh  
        - Range: 725 km  
        - Higher capacity, lower efficiency
        """)
    
    st.success("Market Implication: Efficiency engineering matters more than raw battery size for maximum range.")

# Run the app
if __name__ == "__main__":
    show_market_leaders_germany_2024()
