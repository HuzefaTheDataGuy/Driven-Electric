import streamlit as st
from PIL import Image
from io import BytesIO
import base64
import os

def show_conclusions():
    # Header for the conclusions section
    st.header("Conclusions and Future Outlook")
    st.markdown("""
        ### 🔑 Key Takeaways

        - Germany's EV growth is driven by **tech innovation**, **policy support**, and **environmental awareness**.
        - Major milestones include **rising EV adoption**, **shifting consumer behavior**, and **government incentives**.
        - Chinese EV brands are challenging local players with **competitive pricing** and **quality**.
        - Tesla’s sales dropped due to **Musk’s statements** and **rising competition**.
        - Stable charging prices are key to keeping **BEVs attractive**.
        - **Northeast Germany** needs better **charging infrastructure**.

        ---

        ### 🔮 Future Outlook

        - **Continued innovation** in battery technology and expansion of EV infrastructure will play a crucial role in shaping the market.
        - **Strong regulatory policies** will further accelerate the transition to electric vehicles.
        - **Modest Overall Growth**: The total passenger vehicle market is expected to grow by only **1%**, reaching approximately **2.84 million units**, still below pre-pandemic levels.
        - **Surge in BEV Sales**: BEV sales are projected to increase by **75%**, totaling around **666,000 units**, driven by stricter EU CO₂ emission regulations. 
        - **Rise in Electrified Vehicle Sales**: Combined sales of BEVs and PHEVs are forecasted to grow by **53%**, reaching approximately **873,000 units**.
        - **Increase in Electric Vehicle Production**: Domestic production is expected to rise by **24%**, with BEV production up by **30%** to **1.39 million units**, solidifying Germany's position as a leading EV manufacturer. 
        - **Slight Growth in Overall Production and Exports**: Total car production and exports are anticipated to grow by **less than 2%**, indicating a focus on **quality and efficiency** over volume.

        ---

        ### 🏛️ Government Incentives for EVs in Germany (2025)

        - **Tax Relief for Electric Company Cars**:  
        Companies can deduct up to **40%** of the value of electric vehicles from their tax bill in the first year, with reductions over time. *(Reuters)*

        - **Vehicle Tax Exemption**:  
        Electric vehicles are **exempt from vehicle tax until 2035**. *(Reuters)*

        - **Hydrogen Infrastructure Support**:  
        The government is investing in **hydrogen refueling infrastructure** for commercial vehicles. *(Reuters)*

        - **"Made in Germany" Premium**:  
        A proposed **10% tax refund** on business investments in **German-made electric cars**. *(Reuters)*
    """, unsafe_allow_html=True)
    # Spacer
    st.markdown("<br>", unsafe_allow_html=True)


    # Centered title
    st.markdown(
        """
        <h2 style="text-align: center; font-size: 30px;">Prepared By TEAM</h2>
        """,
        unsafe_allow_html=True
    )

    # Load and display image
    image_path = os.path.join(os.path.dirname(__file__), 'images', 'team_double_trouble.png')
    if os.path.exists(image_path):
        team_double_trouble = Image.open(image_path)
        buffered = BytesIO()
        team_double_trouble.save(buffered, format="PNG")
        img_b64 = base64.b64encode(buffered.getvalue()).decode()

        st.markdown(
            f"""
            <div style="display: flex; justify-content: center; align-items: center;">
                <img src="data:image/png;base64,{img_b64}" style="width:90%; max-width:300px;">
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.error(f"Image not found: {image_path}")

    # Spacer
    st.markdown("<br>", unsafe_allow_html=True)

    # Two columns for team members
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            <div style="text-align: right; font-size: 20px;">
                <strong>👨‍💻 Huzefa Ahmed</strong><br>
                <a href="https://www.linkedin.com/in/muhammadhuzefaahmed/" target="_blank">LinkedIn</a><br><br>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div style="text-align: left; font-size: 20px;">
                <strong>👩‍💻 Elena Vasilevskaya</strong><br>
                <a href="https://www.linkedin.com/in/elena-vasilevskaya-004420122/" target="_blank">LinkedIn</a><br><br>
            </div>
            """,
            unsafe_allow_html=True
        )

    # Final thank you note
    st.markdown(
        """
        <h2 style="text-align: center; font-size: 40px;"><strong>THANK YOU FOR YOUR ATTENTION ! 🎉😌</strong></h2>
        """,
        unsafe_allow_html=True
    )
