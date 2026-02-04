import pandas as pd
import numpy as np

class StrategyAnalyzer:
    def __init__(self, session):
        self.session = session
        self.laps = session.laps
    
    def classify_strategies(self, strategies):
        """Group drivers by number of stops"""
        strategy_groups = {}
        for strat in strategies:
            stops = strat['TotalStops']
            if stops not in strategy_groups:
                strategy_groups[stops] = []
            strategy_groups[stops].append(strat['Driver'])
        return strategy_groups
    
    def compare_stint_pace(self, driver1, driver2, stintnum = 1):
        """Compare lap times between two drivers in same stint"""
        d1_laps = self.laps[(self.laps['Driver'] == driver1) & 
                            (self.laps['Stint'] == stint_num)]
        d2_laps = self.laps[(self.laps['Driver'] == driver2) & 
                            (self.laps['Stint'] == stint_num)]
        return {
            'driver1': driver1,
            'driver2': driver2,
            'avg_laptime_d1': d1_laps['LapTime'].mean().total_seconds(),
            'avg_laptime_d2': d2_laps['LapTime'].mean().total_seconds(),
            'compound_d1': d1_laps['Compound'].iloc[0] if len(d1_laps) >0 else None,
            'compound_d2': d2_laps['Compound'].iloc[0] if len(d2_laps) >0 else None 
        }
    
    def tire_degradation(self, driver, stint_num=1):
        """Calculate tire degradation rate per lap"""
        stint_laps = self.laps[(self.laps['Driver']==driver),
                               (self.laps['Stint'] == stint_num)]
        
        if len(stint_laps) < 3:
            return None
        
        stint_laps['LapTimeSec'] = stint_laps['LapTime'].dt.total_seconds()

        x = stint_laps['TyreLife'].values
        y = stint_laps['LapTimeSec'].values

        if len(x) > 1:
            slope = np.polyfit(x,y, 1)[0]
            return slope
        return None