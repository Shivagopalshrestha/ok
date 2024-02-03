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
        # ... (your ticker data)
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
