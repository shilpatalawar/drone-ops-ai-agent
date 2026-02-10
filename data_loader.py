import pandas as pd

# ==============================
# Google Sheets CSV Export URLs
# ==============================

# Pilot Roster Sheet
PILOT_SHEET_URL = (
    "https://docs.google.com/spreadsheets/d/"
    "1wa2KRYKinK6-wRcNIPiBS_bIKtZHazvHK-UthKqGXIo"
    "/export?format=csv&gid=619085810"
)

# Drone Fleet Sheet
DRONE_SHEET_URL = (
    "https://docs.google.com/spreadsheets/d/"
    "1g4d2KwlHqEnGeUpr1MZqMisq_g_6Giuh_lPXNKm8K1o"
    "/export?format=csv&gid=2101896803"
)

# Missions Sheet
MISSION_SHEET_URL = (
    "https://docs.google.com/spreadsheets/d/"
    "1op_b4f14sdy3KwwoUJfHAWy1kuA1mImpz7gOZRsHIro"
    "/export?format=csv&gid=44624968"
)

# ==============================
# Loaders (Google Sheets = DB)
# ==============================

def load_pilots():
    return pd.read_csv(PILOT_SHEET_URL)


def load_drones():
    return pd.read_csv(DRONE_SHEET_URL)


def load_missions():
    return pd.read_csv(MISSION_SHEET_URL)
