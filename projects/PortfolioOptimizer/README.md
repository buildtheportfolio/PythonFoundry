# Stock Market Portfolio Optimization App

This interactive Python web app is built using **Streamlit**, based on Modern Portfolio Theory (MPT). It pulls real-time historical data from Yahoo Finance and uses Monte Carlo simulation to identify the optimal mix of stocks for maximum risk-adjusted return (Sharpe Ratio).

## Local Development

If you want to run this application locally on your machine:

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Start the Streamlit application:
   ```bash
   streamlit run app.py
   ```

## Deploying

This project is structured perfectly so that it can be deployed with zero-configuration on **Streamlit Community Cloud**, huggingface spaces, or anywhere else that supports standard python applications.

### Option 1: Streamlit Community Cloud (Recommended)
1. Push this directory to a GitHub repository.
2. Go to [share.streamlit.io](https://share.streamlit.io) and sign in.
3. Click **New app**.
4. Select the repository and set the main file path to `app.py`.
5. Click **Deploy**. Your app will be live and shareable in under a minute!

### Option 2: Render or Heroku
1. Create an account on Render or Heroku.
2. Link your GitHub repository.
3. Define the start command for the web service as:
   ```bash
   streamlit run app.py --server.port $PORT
   ```
4. Deploy the service!

## About the implementation
- **yfinance**: For streaming free stock market historical data.
- **pandas & numpy**: Used to compute expected standard deviations, co-variance matrices, and annualized volatility stats.
- **matplotlib & seaborn**: Used to generate sleek and comprehensive data visualizations.
