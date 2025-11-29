import requests
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

st.title("📈 Bitcoin Price Tracker")
st.write("Data from CoinGecko (Last 24 Hours)")


url = (
    "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=1"
)
response = requests.get(url)
data = response.json()


df = pd.DataFrame(data["prices"], columns=["timestamp", "price"])


df["time"] = pd.to_datetime(df["timestamp"], unit="ms")


fig, ax = plt.subplots()
ax.plot(df["time"], df["price"])
ax.set_xlabel("Time")
ax.set_ylabel("Price (USD)")
ax.set_title("Bitcoin Price (Last 24 Hours)")
plt.xticks(rotation=45)
plt.tight_layout()


st.pyplot(fig)


st.subheader("Raw Price Data")
st.dataframe(df)
