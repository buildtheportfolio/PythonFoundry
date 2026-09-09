import streamlit as st
import pandas as pd
import yfinance as yf
from datetime import date, timedelta
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Page configuration
st.set_page_config(page_title="Stock Portfolio Optimizer", page_icon="📈", layout="wide")

st.title("📈 Stock Market Portfolio Optimization")
st.markdown("""
This app applies **Modern Portfolio Theory (MPT)** to find the optimal stock portfolio allocation. 
It retrieves historical stock data, calculates expected returns and volatilities, generates thousands of simulated portfolios, and identifies the allocation that maximizes the Sharpe Ratio.
""")

@st.cache_data(show_spinner=False)
def fetch_stock_data(tickers, start_date, end_date):
    """Fetch historical stock data and abstract away yfinance format variations."""
    data = yf.download(tickers, start=start_date, end=end_date, progress=False)
    if data.empty:
        return pd.DataFrame()
        
    # Depending on yfinance version and single vs multi-ticker, handle column structure
    if isinstance(data.columns, pd.MultiIndex):
        if 'Adj Close' in data.columns.levels[0]:
            adj_close = data['Adj Close']
        else:
            adj_close = data['Close']
    else:
        # Single ticker case or flat dataframe
        if 'Adj Close' in data.columns:
            adj_close = pd.DataFrame({tickers[0]: data['Adj Close']})
        else:
            adj_close = pd.DataFrame({tickers[0]: data['Close']})
            
    return adj_close.dropna()

with st.sidebar:
    st.header("⚙️ Configuration")
    tickers_input = st.text_input("Enter Tickers (comma-separated)", "RELIANCE.NS, TCS.NS, INFY.NS, HDFCBANK.NS")
    tickers = [ticker.strip().upper() for ticker in tickers_input.split(",") if ticker.strip()]
    
    st.caption("E.g.: AAPL, MSFT, GOOG, TSLA")
    
    years_back = st.slider("Lookback Period (Years)", 1, 10, 1)
    num_portfolios = st.number_input("Number of Simulated Portfolios", min_value=1000, max_value=50000, value=10000, step=1000)
    
    run_optimization = st.button("Run Optimization", type="primary", use_container_width=True)

if run_optimization:
    if len(tickers) < 2:
        st.warning("Portfolio optimization requires at least 2 tickers to find the optimal blend.")
        st.stop()
        
    st.markdown("---")
    
    end_date = date.today().strftime("%Y-%m-%d")
    start_date = (date.today() - timedelta(days=years_back * 365)).strftime("%Y-%m-%d")
    
    with st.spinner("Fetching stock data..."):
        try:
            adj_close = fetch_stock_data(tickers, start_date, end_date)
            if adj_close.empty:
                st.error("Could not fetch data for the given tickers. Please check the symbols.")
                st.stop()
        except Exception as e:
            st.error(f"Error fetching data: {e}")
            st.stop()

    # Filter out tickers that might have failed to download (missing columns)
    valid_tickers = [t for t in tickers if t in adj_close.columns]
    
    if len(valid_tickers) < 2:
        st.error("Could not fetch sufficient valid data for the requested tickers.")
        st.stop()

    st.subheader("📊 Historical Performance")
    tab1, tab2, tab3 = st.tabs(["Prices Over Time", "Daily Returns Distribution", "Correlation Matrix"])
    
    with tab1:
        st.markdown("**Adjusted Close Price Over Time**")
        fig_price = plt.figure(figsize=(14, 6))
        sns.set_style('whitegrid')
        
        for ticker in valid_tickers:
            sns.lineplot(data=adj_close, x=adj_close.index, y=ticker, label=ticker)
            
        plt.xlabel('Date', fontsize=12)
        plt.ylabel('Price', fontsize=12)
        plt.legend(title='Ticker')
        st.pyplot(fig_price)
        
    # Calculate daily returns
    daily_returns = adj_close.pct_change().dropna()
    
    with tab2:
        st.markdown("**Distribution of Daily Returns**")
        fig_dist = plt.figure(figsize=(14, 6))
        sns.set_style('whitegrid')
        
        for ticker in valid_tickers:
            sns.histplot(daily_returns[ticker], bins=50, kde=True, label=ticker, alpha=0.5)
            
        plt.xlabel('Daily Return', fontsize=12)
        plt.ylabel('Frequency', fontsize=12)
        plt.legend(title='Ticker')
        st.pyplot(fig_dist)
        
    with tab3:
        st.markdown("**Correlation Matrix of Daily Returns**")
        corr_matrix = daily_returns.corr()
        fig_corr = plt.figure(figsize=(10, 8))
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=.5, fmt='.2f')
        st.pyplot(fig_corr)
        
    st.markdown("---")
    st.subheader("🎯 Optimizing Portfolio (Modern Portfolio Theory)")
    
    with st.spinner("Running Monte Carlo simulations..."):
        # Standard assumption of 252 trading days in a year
        trading_days = 252
        expected_returns = daily_returns.mean() * trading_days
        cov_matrix = daily_returns.cov() * trading_days
        
        st.markdown("**Annualized Expected Return & Volatility per Stock**")
        stock_stats = pd.DataFrame({
            'Expected Return': expected_returns,
            'Volatility': daily_returns.std() * np.sqrt(trading_days)
        })
        
        # Style dataframe numbers as percentages
        st.dataframe(
            stock_stats.style.format("{:.2%}"), 
            use_container_width=True
        )
        
        # Monte Carlo Simulation
        results = np.zeros((3, num_portfolios))
        weights_record = []
        
        for i in range(num_portfolios):
            weights = np.random.random(len(valid_tickers))
            weights /= np.sum(weights)
            weights_record.append(weights)
            
            portfolio_return = np.dot(weights, expected_returns)
            portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
            
            results[0,i] = portfolio_return
            results[1,i] = portfolio_volatility
            results[2,i] = portfolio_return / portfolio_volatility # Sharpe Ratio
            
        max_sharpe_idx = np.argmax(results[2])
        max_sharpe_return = results[0, max_sharpe_idx]
        max_sharpe_volatility = results[1, max_sharpe_idx]
        max_sharpe_ratio = results[2, max_sharpe_idx]
        optimal_weights = weights_record[max_sharpe_idx]
        
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("**Efficient Frontier Simulation**")
        fig_frontier = plt.figure(figsize=(10, 7))
        scatter = plt.scatter(results[1,:], results[0,:], c=results[2,:], cmap='YlGnBu', marker='o', s=10, alpha=0.3)
        plt.colorbar(scatter, label='Sharpe Ratio')
        plt.scatter(max_sharpe_volatility, max_sharpe_return, marker='*', color='r', s=500, label='Maximum Sharpe Ratio')
        plt.title('Efficient Frontier')
        plt.xlabel('Volatility (Risk)')
        plt.ylabel('Expected Return')
        plt.legend(labelspacing=0.8)
        st.pyplot(fig_frontier)
        
    with col2:
        st.markdown("### Optimal Portfolio")
        st.info("The portfolio with the best risk-adjusted return (Maximum Sharpe Ratio).")
        
        st.metric("Expected Annual Return", f"{max_sharpe_return * 100:.2f}%")
        st.metric("Annual Volatility (Risk)", f"{max_sharpe_volatility * 100:.2f}%")
        st.metric("Sharpe Ratio", f"{max_sharpe_ratio:.2f}")
        
        st.markdown("**Optimal Allocation Weights:**")
        portfolio_weights_df = pd.DataFrame({
            'Ticker': valid_tickers,
            'Weight': [f"{w * 100:.2f}%" for w in optimal_weights]
        })
        st.dataframe(portfolio_weights_df, hide_index=True, use_container_width=True)
