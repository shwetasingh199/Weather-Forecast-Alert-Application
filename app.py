import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from src.api_fetch import fetch_weather

# PAGE CONFIG

st.set_page_config(
    page_title="Weather Forecast App",
    layout="wide"
)

st.title("🌦 Weather Forecast & Alert Application")

# =========================
# SIDEBAR
# =========================

st.sidebar.header("⚙ Dashboard Settings")

mode = st.sidebar.radio(
    "Select Dashboard Mode",
    [
        "🌐 Live API Dashboard",
        "🧪 Simulation Dashboard"
    ]
)

# =========================
# LIVE API MODE
# =========================

if mode == "🌐 Live API Dashboard":

    city = st.sidebar.selectbox(
        "Select City",
        [
            "Delhi",
            "Mumbai",
            "Patiala",
            "Chandigarh",
            "Bangalore"
        ]
    )

    if st.sidebar.button("Fetch Live Weather"):

        try:

            data = fetch_weather(city)

            hourly = data["hourly"]

            dates = hourly["time"][:12]

            temperatures = hourly["temperature_2m"][:12]

            humidity = hourly["relative_humidity_2m"][:12]

            rain = hourly["precipitation"][:12]

            wind = hourly["wind_speed_10m"][:12]

            # DATAFRAME

            df = pd.DataFrame({
                "Date": dates,
                "Temperature": temperatures,
                "Humidity": humidity,
                "Rain": rain,
                "Wind Speed": wind
            })

            # SUMMARY

            st.subheader(f"📍 Live Weather Summary — {city}")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    "🌡 Avg Temp",
                    f"{round(df['Temperature'].mean(),1)} °C"
                )

            with col2:
                st.metric(
                    "💧 Avg Humidity",
                    f"{round(df['Humidity'].mean(),1)} %"
                )

            with col3:
                st.metric(
                    "🌧 Total Rain",
                    f"{round(df['Rain'].sum(),1)} mm"
                )

            # TABLE

            st.subheader("📋 Forecast Data")

            st.dataframe(df)

            # ALERTS

            st.subheader("🚨 Smart Alerts")

            alert_found = False

            for i in range(len(df)):

                if temperatures[i] > 40:
                    st.error(
                        f"🔥 Heat Alert on {dates[i]}"
                    )
                    alert_found = True

                if humidity[i] > 85:
                    st.warning(
                        f"💧 High Humidity Alert on {dates[i]}"
                    )
                    alert_found = True

                if rain[i] > 0:
                    st.info(
                        f"🌧 Rain Alert on {dates[i]}"
                    )
                    alert_found = True

                if wind[i] > 25:
                    st.warning(
                        f"💨 High Wind Alert on {dates[i]}"
                    )
                    alert_found = True

            if not alert_found:
                st.success(
                    "✅ No Extreme Weather Alerts"
                )

            # CHART

            st.subheader("📈 Temperature Forecast")

            fig, ax = plt.subplots(figsize=(12,5))

            ax.plot(
                df["Date"],
                df["Temperature"],
                marker="o"
            )

            plt.xticks(rotation=45)

            st.pyplot(fig)

            # DOWNLOAD

            csv = df.to_csv(index=False)

            st.download_button(
                "📥 Download Live Report",
                csv,
                f"{city}_forecast.csv",
                "text/csv"
            )

        except Exception as e:

            st.error(f"Error: {e}")

# =========================
# SIMULATION MODE
# =========================

if mode == "🧪 Simulation Dashboard":

    st.subheader("🧪 Simulated Extreme Weather Dashboard")

    df = pd.read_csv(
        "data/simulated_weather.csv"
    )

    st.dataframe(df)

    # METRICS

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "🔥 Max Temp",
            f"{df['temp'].max()} °C"
        )

    with col2:
        st.metric(
            "💧 Max Humidity",
            f"{df['humidity'].max()} %"
        )

    with col3:
        st.metric(
            "🌧 Total Rain",
            f"{df['rain'].sum()} mm"
        )

    # ALERTS

    st.subheader("🚨 Simulated Alerts")

    for index, row in df.iterrows():

        if row["temp"] > 40:
            st.error(
                f"🔥 Heat Alert on {row['date']}"
            )

        if row["humidity"] > 85:
            st.warning(
                f"💧 Humidity Alert on {row['date']}"
            )

        if row["rain"] > 0:
            st.info(
                f"🌧 Rain Alert on {row['date']}"
            )

        if row["wind"] > 25:
            st.warning(
                f"💨 Wind Alert on {row['date']}"
            )

    # GRAPH

    st.subheader("📈 Simulated Temperature Forecast")

    fig2, ax2 = plt.subplots(figsize=(12,5))

    ax2.plot(
        df["date"],
        df["temp"],
        marker="o"
    )

    plt.xticks(rotation=45)

    st.pyplot(fig2)

    # DOWNLOAD

    csv2 = df.to_csv(index=False)

    st.download_button(
        "📥 Download Simulation Report",
        csv2,
        "simulation_report.csv",
        "text/csv"
    )