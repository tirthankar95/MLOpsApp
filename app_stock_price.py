import streamlit as st 
import yfinance as yf 
import datetime 

ticker_symbol = st.text_input("Enter company ticker:", "GOOG")
col1, col2 = st.columns(2)
with col1:
    start_date = st.date_input("Enter start date:", datetime.date(2019, 1, 1))
with col2:
    end_date = st.date_input("Enter end date", datetime.date(2020, 1, 1))

ticker_data = yf.Ticker(ticker_symbol)
ticker_df = ticker_data.history(period = "1d", start = start_date,\
                                end = end_date)
st.dataframe(ticker_df, use_container_width=True)
st.write(f'Line Chart of {ticker_symbol}')
st.line_chart(ticker_df.Close)