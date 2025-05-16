import streamlit as st

st.set_page_config(layout="wide")
from introduction import show_introduction
from market_leaders_germany_2024 import show_market_leaders_germany_2024
from market_observation import show_market_observation
from ev_segment_evolution import show_ev_segment_evolution
from ev_charging_trends import show_charging_trends
from charging_infrastructure_overview import show_charging_infrastructure_overview
from conclusions import show_conclusions

# Main application entry point
def main():

    # Sidebar navigation
    st.sidebar.title("Navigation")
    pages = {
        "Introduction": show_introduction,
        "BEV Leaders Germany 2024": show_market_leaders_germany_2024,
        "Market Observation" : show_market_observation,
        "EV Segment Evolution": show_ev_segment_evolution,
        "EV Charging Trends": show_charging_trends,
        "Charging Infrastructure Overview": show_charging_infrastructure_overview,
        "Conclusions": show_conclusions,
    }

    selected_page = st.sidebar.radio("Go to", list(pages.keys()))

    # Render the selected page
    pages[selected_page]()


if __name__ == "__main__":
    main()