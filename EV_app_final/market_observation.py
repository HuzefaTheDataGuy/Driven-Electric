import streamlit as st
from streamlit.components.v1 import html
from PIL import Image
import base64
from io import BytesIO

def show_market_observation():
    st.header("German BEV Market Observation over past 5 years")

    st.subheader("Key Highlights")

    st.markdown("""
    - This analysis compares the **German BEV market** with the broader **European market**.
    - The BEV market declined in 2024 — both in **Germany** and across **Europe**.
    - **Škoda** was the only brand among the top five to show **growth**, increasing its BEV sales by **+1,809 units** compared to the previous year.
    - All other top four brands — **Volkswagen**, **BMW**, **Tesla**, and **Mercedes** — experienced a **decline in BEV sales**.
    - **Tesla**, which had performed strongly globally and in Germany until 2023, saw a **significant drop** in sales in 2024.
    - According to several 2025 market reports, **Tesla is no longer among the top 5 BEV brands in Germany**.
    - **Škoda**, now ranked 5th, continues to perform strongly in Germany — a **key market for its BEV sales**.
    """)

    # Tableau visualization
    tableau_embed_code = """
    <div style="width:100%; height:800px;">
        <iframe 
            src="https://public.tableau.com/views/BEVsSalesTrendinGermanyvsEurope/EVDEEuropeSalesTrends?:showVizHome=no&:embed=true"
            width="100%" 
            height="100%" 
            frameborder="0" 
            style="border:none;">
        </iframe>
    </div>
    """

    html(tableau_embed_code, height=800)

    st.markdown(
        """
        <h2 style="text-align: center; font-size: 25px; margin-bottom: 30px;">
        Tesla Sales Drop in Europe 
        </h2> 
        """, unsafe_allow_html=True
    )

    # Markdown text
    st.markdown("""
    Tesla’s sales fell in several European markets in March, according to data published by Reuters. The news agency reports that the new figures add signs that drivers are turning away from Elon Musk’s electric car brand as competition from Chinese car manufacturers increases and some protest his political views.  
    <br> Tesla’s quarterly sales fell by around 62 percent in Germany, 55 percent in Sweden and Denmark, almost 50 percent in the Netherlands, and 41 percent in France. The United Kingdom continues to be Tesla's biggest market in Europe and was the only country in the continent to see a sales increase in the first quarter of 2025 (+3.5 percent). Nevertheless, Tesla's share of the UK market fell by more than 4 percentage points to 10.7 percent last month, partly due to increased competition from other manufacturers in a rapidly growing market (the country recorded record electric vehicle sales in the first quarter).
    """, unsafe_allow_html=True)

    tesla_drop = Image.open('./images/tesla_drop.png')

        # Convert image to base64
    buffered = BytesIO()
    tesla_drop.save(buffered, format="PNG")
    img_b64 = base64.b64encode(buffered.getvalue()).decode()

        # Display image in the center using HTML
    st.markdown(
        f"""
        <div style="display: flex; justify-content: center; align-items: center;">
        <img src="data:image/png;base64,{img_b64}" style="width:90%; max-width:500px;">
        </div>
        """,
            unsafe_allow_html=True
        )
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.divider()
