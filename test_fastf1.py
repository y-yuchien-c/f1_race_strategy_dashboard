import fastf1

fastf1.Cache.enable_cache('./data/cache')

session = fastf1.get_session(2024, 'Bahrain', 'R')
print("Loading session...")
session.load()

print(f"Session loaded: {session.event['EventName']}")
print(f"Total laps: {len(session.laps)}")
print(f"Drivers: {session.laps['Driver'].unique()}")