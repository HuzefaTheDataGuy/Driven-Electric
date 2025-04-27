import streamlit as st
from PIL import Image
import base64
from io import BytesIO

def show_introduction():
    # Title of the page
    st.markdown(
        """
        <h1 style="text-align: center; font-size: 45px; margin-bottom: 30px;">
        The Transformation of Germany’s Electric Vehicle Market 
        </h1> <br><br>
        <p style="text-align: left; font-size: 25px; margin-top: -10px;">
        <strong>Main Research Question:</strong> How Germany’s EV market has changed over the past years, and what are the key drivers and influential factors behind these changes? 
        </p> <br>
        """, unsafe_allow_html=True
    ) 

    # Observation 
    
    st.markdown(
        """
        <h2 style="text-align: center; font-size: 25px;">General Observation</h2>
        <div style="text-align: justify; font-size: 16px;">
        <p>
        This analysis was conducted as the final project during the Spiced Academy Bootcamp, as part of the educational process. It focuses on the Battery Electric Vehicle (BEV) market in Germany over the past five years, highlighting market leaders and top-selling models. The study also explores customer preferences across different vehicle types, examines the development of charging infrastructure, analyses trends in EV charging prices, and identifies key factors influencing the growth of the BEV market.
        </p>
        </div>""", unsafe_allow_html=True
    )

     # Key definitions
    st.markdown(
        """ 
        <br>
        <h2 style="text-align: center; font-size: 25px;">Key Terms & Definitions</h2>
        <div style="text-align: justify; font-size: 16px;">
        <br>
        <strong>EV</strong> – Electric Vehicle  <br>
        <i>(Any vehicle powered by electricity)</i> <br><br>

        **BEV** – Battery Electric Vehicle  
        *(Fully electric, no gas engine)*  

        **Non-BEV** – Other Electric Vehicle   
        *(Includes Hybrid Cars and Plug-in Hybrids)* 

        **AC** – Alternating Current  
        *(Used in regular/slow charging)*  

        **DC** – Direct Current  
        *(Used in fast charging)* 
        <br>
        </div> """, unsafe_allow_html=True
    )
    
    
    
    # Resourses
    
    st.markdown(
        """
        <h2 style="text-align: center; font-size: 25px;"> Used Resourses</h2>
        <div style="text-align: justify; font-size: 16px;">
        The analysis is based on data from <strong>official annual reports</strong> and <strong>government sources</strong>, including the Kraftfahrt-Bundesamt (KBA), Bundesnetzagentur, and the Federal Ministry for Economic Affairs and Climate Action (BMWK). It also incorporates <strong>open data sourses</strong> such as Kaggle, Statista, the International Energy Agency (IEA), Cardino, and Tankerkönig. In addition, <strong>topic-specific articles</strong> were reviewed to gain deeper insights into the current market landscape
        </div>
        """, unsafe_allow_html=True
    )
    st.markdown("<br><br>", unsafe_allow_html=True)

    #Tech Stack
    st.markdown(
        """
        <h2 style="text-align: center; font-size: 25px;"> Tech Stack</h2>
        <div style="text-align: justify; font-size: 16px;">
        <p>
        The analysis was conducted using Python, with libraries such as Pandas, NumPy, and PostgreSQL for data manipulation. Streamlit was used to create an interactive dashboard for presenting the findings. 
        Tableau was also utilized for advanced data visualization and embedding interactive charts. 
        A complete list of the tools and programs used in this project can be found in the visualization below.
    
         </p>
        </div> """, unsafe_allow_html=True
    )

        #Load the image
    logos = Image.open('./images/logos.png')

    # Convert image to base64
    buffered = BytesIO()
    logos.save(buffered, format="PNG")
    img_b64 = base64.b64encode(buffered.getvalue()).decode()

    # Display image in the center using HTML
    st.markdown(
        f"""
        <div style="display: flex; justify-content: center; align-items: center;">
            <img src="data:image/png;base64,{img_b64}" style="width:90%; max-width:1000px;">
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown("<br><br>", unsafe_allow_html=True)

        # Horizontal divider
    st.markdown("---")


    # Title centered
    st.markdown(
        """
        <h2 style="text-align: center; font-size: 20px;">Prepared By Team DOUBLE TROUBLE (Elena Vasilevskaya, Huzefa Ahmed)</h2>
        """,
        unsafe_allow_html=True
    )
