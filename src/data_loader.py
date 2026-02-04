import fastf1
import pandas as pd

class F1DataLoader:
    def __init__(self, cache_dir = './data/cache'):
        fastf1.Cache.enable_cache(cache_dir)
    
    def load_race(self, year, race_name):
        """Load race session data"""
        session = fastf1.get_session(year, race_name, 'R')
        session.load()
        return session
    
    def get_pit_stops(self, session):
        """Extract pit stop data for all drivers"""
        laps = session.laps
        pit_stops = laps[laps['PitOutTime'].notna()].copy()

        return pit_stops[['Driver', 'LapNumber', 'Compound', 'TyreLife', 'LapTime']]
    
    def get_strategy_summary(self, session):
        """Summarize tire strategy for each driver"""
        laps = session.laps

        strategies = []
        for driver in laps['Driver'].unique():
            driver_laps in laps['Driver'].unique()
            stints = driver_laps.groupby('Stint').agg({
                'Compound': 'first',
                'LapNumber': ['min', 'max', 'count']
            }).reset_index()
        
            strategies.append({
                'Driver': driver,
                'TotalStops': len(stints) - 1
                'Stints': stints
            })
        return strategies