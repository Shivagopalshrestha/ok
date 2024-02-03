import streamlit as st
import yfinance as yf
import pandas as pd

def fetch_revenue_data(symbols):
    revenue_data = {}

    for symbol in symbols:
        try:
            stock = yf.download(symbol, start="2020-01-01", end="2022-01-01")
            if not stock.empty and 'Close' in stock.columns:
                revenue_data[symbol] = stock['Close'].mean()
            else:
                st.warning(f"No revenue data available for {symbol}.")
        except Exception as e:
            st.error(f"Error fetching data for {symbol}: {e}")

    return revenue_data

def main():
    st.title("NASDAQ 100 Revenue Growth Monitoring App")

    # Step 1: Retrieve NASDAQ 100 stock symbols
    nasdaq_100_tickers = {
    'AAPL': 'Apple Inc.',
    'MSFT': 'Microsoft Corporation',
    'AMZN': 'Amazon.com Inc.',
    'GOOGL': 'Alphabet Inc. Class A',
    'GOOG': 'Alphabet Inc. Class C',
    'TSLA': 'Tesla Inc.',
    'FB': 'Meta Platforms, Inc. (formerly Facebook Inc.)',
    'NVDA': 'NVIDIA Corporation',
    'PYPL': 'PayPal Holdings, Inc.',
    'ADBE': 'Adobe Inc.',
    'INTC': 'Intel Corporation',
    'ASML': 'ASML Holding N.V.',
    'CMCSA': 'Comcast Corporation',
    'CSCO': 'Cisco Systems, Inc.',
    'NFLX': 'Netflix Inc.',
    'PEP': 'PepsiCo, Inc.',
    'TMUS': 'T-Mobile US, Inc.',
    'AVGO': 'Broadcom Inc.',
    'AMGN': 'Amgen Inc.',
    'COST': 'Costco Wholesale Corporation',
    'QCOM': 'Qualcomm Incorporated',
    'TXN': 'Texas Instruments Incorporated',
    'ACN': 'Accenture plc',
    'AMAT': 'Applied Materials, Inc.',
    'INTU': 'Intuit Inc.',
    'IBM': 'International Business Machines Corporation',
    'MU': 'Micron Technology, Inc.',
    'LRCX': 'Lam Research Corporation',
    'GILD': 'Gilead Sciences, Inc.',
    'FISV': 'Fiserv, Inc.',
    'BKNG': 'Booking Holdings Inc.',
    'ADP': 'Automatic Data Processing, Inc.',
    'REGN': 'Regeneron Pharmaceuticals, Inc.',
    'AMD': 'Advanced Micro Devices, Inc.',
    'ISRG': 'Intuitive Surgical, Inc.',
    'EXC': 'Exelon Corporation',
    'WBA': 'Walgreens Boots Alliance, Inc.',
    'BIDU': 'Baidu, Inc.',
    'AAL': 'American Airlines Group Inc.',
    'ATVI': 'Activision Blizzard, Inc.',
    'CTSH': 'Cognizant Technology Solutions Corporation',
    'ORLY': "O'Reilly Automotive, Inc.",
    'JD': 'JD.com, Inc.',
    'VRTX': 'Vertex Pharmaceuticals Incorporated',
    'CSX': 'CSX Corporation',
    'MELI': 'MercadoLibre, Inc.',
    'LULU': 'Lululemon Athletica Inc.',
    'WDAY': 'Workday, Inc.',
    'PDD': 'Pinduoduo Inc.',
    'EA': 'Electronic Arts Inc.'
        }
    nasdaq100_symbols = nasdaq_100_tickers.keys()

    # Step 2: Fetch revenue data
    revenue_data = fetch_revenue_data(nasdaq100_symbols)

    # Step 3: Store and analyze data
    revenue_df = pd.DataFrame(list(revenue_data.items()), columns=['Symbol', 'Mean Revenue'])

    # Step 4: Monitor growth
    revenue_df['Revenue Growth'] = revenue_df['Mean Revenue'].pct_change() * 100

    # Step 5: Display results
    st.dataframe(revenue_df)

if __name__ == "__main__":
    main()
