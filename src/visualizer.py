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

        strategies_sorted = sorted(strategies, key= lambda x: x['Driver'])

        for i, strat in enumerate(strategies_sorted):
            driver = strat['Driver']
            stints = strat['Stints']
        
            for idx, row in stints.iterrows():
                try:
                    compound = row['Compound']
                    start_lap = int(row['StartLap'])
                    end_lap = int(row['EndLap'])
                    
                    print(f"  Stint: {compound} from lap {start_lap} to {end_lap}")  # Console debug
                    
                    # Each driver gets their own y-value (i)
                    fig.add_trace(go.Scatter(
                        x=[start_lap, end_lap],
                        y=[i, i],
                        mode='lines',
                        line=dict(
                            color=self.COMPOUND_COLORS.get(compound, '#808080'), 
                            width=20
                        ),
                        showlegend=False,
                        hovertemplate=f"<b>{driver}</b><br>Laps {start_lap}-{end_lap}<br>{compound}<extra></extra>"
                    ))
                except Exception as e:
                    print(f"  ERROR plotting stint: {e}")
                    continue
                
        driver_names = [s['Driver'] for s in strategies_sorted]
        
        fig.update_layout(
            title="Race Strategy Timeline - Tire Compounds",
            xaxis_title="Lap Number",
            yaxis_title="Driver",
            yaxis=dict(
                tickmode='array',
                tickvals=list(range(len(driver_names))),
                ticktext=driver_names,
                range=[-0.5, len(driver_names) - 0.5]
            ),
            height=max(800, len(driver_names) * 40),
            hovermode='closest',
            plot_bgcolor='rgba(240,240,240,0.5)'
        )
        
        fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='white')
        fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='white')
        
        return fig
    def plot_pace_comparison(self, laps, drivers):
        """Compare lap times across drivers"""
        import plotly.graph_objects as go
        
        fig = go.Figure()
        
        for driver in drivers:
            driver_laps = laps[laps['Driver'] == driver].copy()
            
            driver_laps = driver_laps[
                (driver_laps['PitOutTime'].isna()) & 
                (driver_laps['LapTime'].notna())
            ]
            
            driver_laps['LapTimeSec'] = driver_laps['LapTime'].dt.total_seconds()
            
            fig.add_trace(go.Scatter(
                x=driver_laps['LapNumber'],
                y=driver_laps['LapTimeSec'],
                mode='lines+markers',
                name=driver,
                hovertemplate=f"<b>{driver}</b><br>Lap: %{{x}}<br>Time: %{{y:.2f}}s<extra></extra>"
            ))
        
        fig.update_layout(
            title="Lap Time Comparison",
            xaxis_title="Lap Number",
            yaxis_title="Lap Time (seconds)",
            hovermode='x unified',
            height=600
        )
        
        return fig