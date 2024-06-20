import pandas as pd
import streamlit as st
import yfinance as yf

st.header('Stock Market Analysis by Rohini :sunglasses:')

ticker_data = yf.Ticker("MSFT")
ticker_df = ticker_data.history(period = "1d", start = "2019-01-01", end = "2024-05-30")
st.dataframe(ticker_df)

st.write('Daily Closing Price Chart')
st.line_chart(ticker_df['Close'])

st.write('Volume Chart')
st.line_chart(ticker_df['Volume'])
