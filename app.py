import streamlit as st
from src.data_loader import F1DataLoader
from src.strategy_analyzer import StrategyAnalyzer
from src.visualizer import StrategyVisualizer

st.set_page_config(page_title = "F1 Strategy Dashboard", layout = "wide")

st.title("🏎️ Formula 1 Race Strategy Dashboard")

st.sidebar.header("Race Selection")
year = st.sidebar.selectbox("Year", [2024, 2023, 2022])
races = ['Bahrain', 'Saudi Arabia', 'Australia', 'Japan', 'Monaco', 'Spain']
race = st.sidebar.selectbox("Grand Prix", races)

@st.cache_data
def load_race_data(year, race, version =2):
    loader = F1DataLoader()
    session = loader.load_race(year, race)
    strategies =loader.get_strategy_summary(session)
    return session, strategies

try:
    with st.spinner("Loading race data..."):
        session, strategies = load_race_data(year, race, version = 2)
    
    st.success(f"Loaded {year} {race} Grand Prix")
    
    # Strategy Overview
    st.header("Strategy Overview")
    analyzer = StrategyAnalyzer(session)
    strategy_groups = analyzer.classify_strategies(strategies)
    
    # ... rest of code

    cols = st.columns(len(strategy_groups))
    for i, (stops, drivers) in enumerate(strategy_groups.items()):
        with cols[i]:
            st.metric(f"{stops}-Stop Strategy", len(drivers))
            st.write(", ".join(drivers))
        
    st.header("Strategy Timeline")
    viz = StrategyVisualizer()
    timeline_fig = viz.plot_strategy_timeline(strategies)
    st.plotly_chart(timeline_fig, use_container_width = True)

    st.header("Driver Pace Comparison")
    all_drivers = [s['Driver'] for s in strategies]
    selected_drivers = st.multiselect("Select drivers to compare", all_drivers, default = all_drivers[:3])

    if selected_drivers:
        pace_fig = viz.plot_pace_comparison(session.laps, selected_drivers)
        st.plotly_chart(pace_fig, use_container_width = True)


    
except Exception as e:
    st.error(f"Error loading data: {str(e)}")
    import traceback
    st.code(traceback.format_exc())  # Show full error trace
    st.info("Make sure you have an internet connection for first-time data download")

            
        