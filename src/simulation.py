import pandas as pd


def run_simulation():

    df = pd.read_csv("data/sample_weather.csv")

    alerts = []

    for index, row in df.iterrows():

        if row["temp"] > 40:
            alerts.append("🔥 Heat Alert")

        if row["humidity"] > 85:
            alerts.append("💧 Humidity Alert")

        if row["rain"] == 1:
            alerts.append("🌧 Rain Alert")

    return df, alerts