import streamlit as st
from streamlit.components.v1 import html as st_html
from PIL import Image
import base64
from io import BytesIO

def show_market_leaders_germany_2024():
    st.header("Germany's EV Market Leaders and Top Models – 2024")

    st.markdown("""
    This section explores Germany's electric vehicle (EV) market in 2024, starting with the top 20 brands by sales, including both BEVs (fully electric) and other EV types.

    We will then focus on the top 5 BEV brands, their best-selling models, and what German drivers are choosing most. Visualizations will highlight popular models, compare their performance and prices, and show the range of BEVs offered by leading manufacturers.
    """)

    # First Visualization
    st.subheader("Top 20 BEV Brands in Germany 2024")
    st_html(
        """
        <div style="width:100%; height:600px; margin-bottom: 30px;">
            <iframe 
                src="https://public.tableau.com/views/Top20BEVBrandsinGermany/BEVnon-BEVSales2024inGermany?:showVizHome=no&:embed=true"
                width="100%" 
                height="100%" 
                frameborder="0" 
                allowfullscreen 
                style="border:none;">
            </iframe>
        </div>
        """, height=600
    )

    # Markdown and embedded HTML
    
    st.markdown("""
    In 2024, the top 5 BEV manufacturers in Germany—**Volkswagen (62,108 units)**, **BMW (42,066)**, **Tesla (37,574)**, **Mercedes (33,991)**, and **Škoda (25,308)**—highlighted the continued dominance of established brands, with Volkswagen leading both the German and broader European markets. This strong performance by European automakers reflects consumer trust in their long-standing reputation for quality and reliability, despite the increasing competitiveness of Chinese EVs.

    The EU's 10% tariff on Chinese EV imports has significantly impacted market dynamics. While this measure protects established German automakers in the short term, it has prompted strategic countermoves from Chinese manufacturers. 

    A prime example is BYD's decision to establish production in Szeged, Hungary - a direct response to circumvent tariff barriers while gaining closer access to European consumers. This shift toward localized manufacturing represents a pivotal moment in China's automotive expansion strategy, transforming what began as a protective measure into a catalyst for deeper market penetration. 
                
    As more Chinese brands likely follow suit, the tariff's long-term effect may ultimately accelerate, rather than prevent, their European market integration.
    """)

    # Embedded Tableau viz (was outside markdown block before — now fixed)
    st_html(
        """
        <div style="margin: 30px 0;">
            <iframe 
                src="https://public.tableau.com/views/BEVModes-Germany2024/TopBEVBrandsinGermany2024?:embed=y&:display_count=yes&:showVizHome=no" 
                width="100%" 
                height="550px" 
                frameborder="0" 
                style="border:none;" 
                allowfullscreen>
            </iframe>
        </div>
        """, height=550
    )

    st.markdown("""
    Tesla, the only non-European brand in the top 5, ranked third. With **100% BEV sales**, Tesla's strong global reputation and leadership in electric mobility likely contributed to its popularity. Notably, the **Tesla Model Y** has been the best-selling EV in Germany and globally over the past three years.          
    """)

    st.divider()

    # Second Visualization
    st.subheader("Most Popular BEV Models in Germany 2024")

    st_html(
        """
        <div style="width:100%; height:600px;">
            <iframe 
                src="https://public.tableau.com/views/CountofBEVModelsfromdifferentManufacturers/EVmodelsfromdifferentbrandgroups?:embed=true&:display_count=yes&:showVizHome=no"
                width="100%" 
                height="100%" 
                frameborder="0" 
                allowfullscreen 
                style="border:none;">
            </iframe>
        </div>
        """, height=600
    )

    st.markdown("**BEV Models per Brand & Top Sellers**")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Top 3 Brands by Model Count")
        st.markdown("""
        1. **Mercedes**: 37 models  
        2. **Porsche**: 18 models  
        3. **Opel / Peugeot / Citroën**: 15 models each
        """)

    with col2:
        st.subheader("Top Selling Models (2024)")
        st.markdown("""
        | Model             | Units Sold     |
        |-------------------|----------------|
        | Tesla Model Y     | 29,896         |
        | Škoda Enyaq       | 25,262         |
        | VW ID.4 & ID.5    | 31,611 (combined) |

        *Tesla Model Y: Best-seller for 3 consecutive years*
        """)

    # Load and show Tesla image 
    st.image('./images/tesla_y.png', width = 600)
  


    # tesla_y = Image.open('./images/tesla_y.png')
    # buffered = BytesIO()
    # tesla_y.save(buffered, format="PNG")
    # img_b64 = base64.b64encode(buffered.getvalue()).decode()

    # st.markdown(
    #     f"""
    #     <div style="display: flex; justify-content: center; align-items: center; margin: 30px 0;">
    #         <img src="data:image/png;base64,{img_b64}" style="width:100%; max-width:400px;">
    #     </div>
    #     """,
    #     unsafe_allow_html=True
    # )

    # Third Visualization
    viz2_url = (
        "https://public.tableau.com/views/BEVModelsinGermany/BEVModelsinGermany"
        "?:embed=y&:showVizHome=no&:toolbar=yes&:display_count=no&:language=en-US"
    )

    st_html(
        f"""
        <div style="width:100%; height:1100px; margin-top: 30px;">
            <iframe 
                src="{viz2_url}"
                width="100%" 
                height="100%" 
                frameborder="0" 
                allowfullscreen 
                style="border:none;">
            </iframe>
        </div>
        """, height=1100
    )

    # Price vs Range
    st.header("Price vs Range Analysis")
    st.markdown("""
    **Key Findings:**
    - Higher price generally means more range
    - Notable price-range benchmarks in the market

    **Standout Examples:**
    - **Tesla Model Y**  
      • Range: 700 km  
      • Price: €95,134  
      • Benchmark for premium segment

    - **VW Group Vehicles**  
      • Consistent range: 350–500 km  
      • Suggests shared battery technology  
      • Popular mid-range choice
    """)
    st.warning("Consumer Insight: Many buyers opt for cheaper models with comparable range to premium alternatives.")
    st.divider()

    # Battery Efficiency
    st.header("Battery Efficiency Comparison")
    st.markdown("**Key Relationships:**")
    st.markdown("""
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
