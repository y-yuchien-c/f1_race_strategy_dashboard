import plotly.graph_objects as go 
import plotly.express as px
import pandas as pd

class StrategyVisualizer:
    COMPOUND_COLORS ={
        'SOFT': '#FF0000',
        'MEDIUM':'#FFF200',
        'HARD': '#EBEBEB',
        'INTERMEDIATE': '#00FF00',
        'WET': '#0000FF'
    }

    def plot_strategy_timeline(self, strategies):
        """Create timeline showing tire strategies"""
        fig = go.Figure()

        for i, strat in enumerate(strategies):
            driver = strat['Driver']
            stinits = strat['Stinits']

            for _, stint in stints,iterrows():
                compound = stint['Compound']
                start_lap = stint[('LapNumber', 'min')]
                end_lap = stint[('LapNumber', 'max')]

                fig.add_trace(go.Scatter(
                    x=[start_lap, end_lap],
                    y=[i,i],
                    mode = 'lines',
                    line = dict(color = self.COMPOUND_COLORS.get(compound, '#808080'), width = 10),
                    name = f"{driver} - {compound}",
                    showlegend = False
                    hovertemplate = f"{driver}<br>Laps {start_lap}-{end_lap}<br>{compound}"
                ))

            fig.update_layout(
                title = "Race Strategy Timeline",
                xaxis_title = "Lap Number",
                yaxis_title = "Driver",
                yaxis = dict(tickmode = 'array', tickvals = list(range(len(strategies))),ticktext=[s['Driver'] for s in strategies]),
                height = 600
            )
            return fig
    
    def plot_pace_comparison(self, laps, drivers):
        """Compare lap times across drivers"""
        fig = go.Figure()

        for driver in drivers:
            driver_laps = laps[laps['Driver']==driver].copy()
            driver_laps['LapTimeSec'] = driver_laps['LapTime'].dt.total_seconds()

            fig.add_trace(go.Scatter(
                x=driver_laps['LapNumber'],
                y=driver_laps['LapTimeSec'],
                mode = 'lines+markers',
                name=driver,
                hovertemplate = f"{driver}<br> Lap: %{{x}} <br> Time: %{{y:.2f}}s"
            ))
        
        fig.update_layout(
            title = "Lap Time Comparison",
            xaxis_title = "Lap Number",
            yaxis_title = "Lap Time (seconds)",
            hovermode = 'x unified'
        )
        return fig