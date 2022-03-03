#Packages:
"""
- Pandas
- Streamlit
- yfinance
"""

import yfinance as yf
import streamlit as st
import pandas as pd
from datetime import date
from plotly import graph_objs as go

@st.cache
def load_data(ticker):
    tickerdata = yf.download(ticker, start_date, end_date)
    tickerdata.reset_index(inplace=True)
    return tickerdata

def plot_full_data():
    fig = go.Figure()
    #fig.add_trace(go.Scatter(x=data['Date'], y=[data.Open, data.Close], name= 'Stock Close'))
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name='Stock Close'))
    #fig.layout.update(title_text='Time Series: {}'.format(ticker), xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)


st.write("""
Stock Visualization App"""
)

st.sidebar.title('Options')
ticker = st.sidebar.selectbox("Select a Ticker:", ('AAPL', 'FB', 'GOOGL'))

start_date = "2015-01-01"
end_date = date.today().strftime("%Y-%m-%d")

st.title("""
{} stock price""".format(ticker))

data_load_state = st.text('Loading Data...')
data = load_data(ticker)
data_load_state.text('Loading Data...Completed')

st.dataframe(data)
plot_full_data()