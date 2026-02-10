import pandas as pd

def load_pilots():
    return pd.read_csv("pilot_roster.csv")

def load_drones():
    return pd.read_csv("drone_fleet.csv")

def load_missions():
    return pd.read_csv("missions.csv")
