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
            driver_laps = laps[laps['Driver'] == driver] 

            driver_laps = driver_laps[driver_laps['Compound'].notna()]

            if len(driver_laps) == 0:
                continue

            stint_data = []
            for stint_num in sorted(driver_laps['Stint'].unique()):
                stint_laps = driver_laps[driver_laps['Stint'] == stint_num]
            
                stint_data.append({
                    'Stint': int(stint_num),
                    'Compound': stint_laps['Compound'].iloc[0],
                    'StartLap': int(stint_laps['LapNumber'].min()),
                    'EndLap': int(stint_laps['LapNumber'].max()),
                    'LapCount': len(stint_laps)
            })
                
            stints = pd.DataFrame(stint_data, columns=['Stint', 'Compound', 'StartLap', 'EndLap', 'LapCount'])

            if len(stints) > 0:
                strategies.append({
                    'Driver': driver,
                    'TotalStops': len(stints) - 1,
                    'Stints': stints
            })
        return strategies