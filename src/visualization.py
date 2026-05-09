import pandas as pd
import matplotlib.pyplot as plt


def create_chart(dates, temperatures):

    df = pd.DataFrame({
        "Date": dates,
        "Temperature": temperatures
    })

    plt.figure(figsize=(10, 5))

    plt.plot(df["Date"], df["Temperature"])

    plt.xticks(rotation=45)

    plt.title("Temperature Forecast")

    plt.xlabel("Date")

    plt.ylabel("Temperature (°C)")

    plt.tight_layout()

    plt.savefig("images/weather_chart.png")

    return df