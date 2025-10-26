import streamlit as st
import pandas as pd
import plotly.express as px

from src.utils import get_weather_data

def main():

    st.set_page_config(page_title="Rain on My Parade", layout="wide")

    st.title("🌧️ Will It Rain On My Parade?")
    st.write("Explore the likelihood of hot, cold, rainy, or windy conditions for your event.")

    # input parameters
    latitude = st.number_input("Latitude", value=40.7128, format="%.4f")   # default NYC
    longitude = st.number_input("Longitude", value=-74.0060, format="%.4f")
    start = st.text_input("Start Year", "2010")
    end = st.text_input("End Year", "2020")

    if st.button("Fetch Data"):
        with st.spinner("Fetching NASA POWER data..."):
            try:
                data = get_weather_data(latitude, longitude, start, end)
                st.success("Data loaded!")
                
                # display data
                st.subheader("Raw Data Preview")
                st.dataframe(data.head())

                # plot temperature distribution
                temp = data["T2M"].dropna()
                fig1 = px.histogram(temp, nbins=40, title="Temperature Distribution (°C)")
                st.plotly_chart(fig1, use_container_width=True)

                # rainfall timeseries
                rain = data["PRECTOTCORR"].dropna()
                fig2 = px.line(rain, title="Daily Rainfall (mm)")
                st.plotly_chart(fig2, use_container_width=True)

                # probability of hot days
                hot_days = (temp > 30).mean() * 100
                st.metric("Probability of Hot Days (>30°C)", f"{hot_days:.1f}%")

                # download csv
                st.download_button(
                    "Download CSV",
                    data.to_csv().encode("utf-8"),
                    "weather_data.csv",
                    "text/csv"
                )
            except Exception as e:
                st.error(f"Error: {e}")

if __name__=="__main__":
    main()