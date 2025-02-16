import streamlit as st
import yfinance as yf
import numpy as np
import plotly.graph_objects as go
from models import black_scholes, monte_carlo, binomial_tree

# Streamlit UI Layout
st.set_page_config(page_title="Options Pricing Platform", layout="wide")

# Intro Page with Instructions
if 'started' not in st.session_state:
    st.session_state.started = False

if not st.session_state.started:
    st.title("Welcome to the Options Pricing Platform!")
    st.markdown("""
    ### Instructions:
    Welcome to the Options Pricing Platform! This application allows you to calculate **call** and **put** option prices using three different pricing models:
    
    1. **Black-Scholes Model** (for European options)
    2. **Monte Carlo Simulation**
    3. **Binomial Tree Model**
    
    To get started, follow these steps:
    
    1. **Input the Parameters**:
       - **Asset Price (S)**: Current price of the underlying asset.
       - **Strike Price (K)**: Price at which the option can be exercised.
       - **Time to Maturity (T)**: The time left until the option expires, in years.
       - **Risk-Free Interest Rate (r)**: Annual risk-free interest rate, typically from treasury bonds.
       - **Volatility (σ)**: The asset's annualized volatility, representing how much the price is expected to fluctuate.

    2. **Model Selection**:
       - Select the option pricing model you wish to use. You can choose from **Black-Scholes**, **Monte Carlo**, or **Binomial Tree**.

    3. **Get Results**:
       - After entering the parameters, click on **Run** to calculate the call and put option prices.
       - Interactive heatmaps will be displayed to visualize the price changes based on different strike prices and stock prices.

    4. **Ticker Option**:
       - You can either input the stock ticker symbol to retrieve the current asset price automatically, or you can manually enter the asset price.
    
    **Click 'Get Started' to proceed and enter the parameters.**
    """)
    if st.button("Get Started"):
        st.session_state.started = True

# Main App - Option Pricing Model
if st.session_state.started:
    # Add name at the top
    st.sidebar.markdown("# Naeem Hussain #\n")
    
    # Sidebar
    st.sidebar.markdown("# 📈 Options Pricing & Volatility Modeling Platform")
    
    # Model selection with radio buttons to ensure only one model is selected at a time
    selected_model = st.sidebar.radio("Select an Option Pricing Model", ["Black-Scholes", "Monte Carlo", "Binomial Tree"])

    # Ticker input
    ticker = st.sidebar.text_input("Enter Ticker Symbol or N/A", "N/A")
    asset_price = None
    if ticker.upper() != "N/A":
        try:
            asset_price = yf.Ticker(ticker).history(period="1d")["Close"].iloc[-1]
            st.sidebar.success(f"Ticker Price: ${asset_price:.2f}")
        except:
            st.sidebar.error("Invalid ticker symbol. Using manual input.")
    
    # Dynamic input fields based on the selected model
    if selected_model:
        S = asset_price if asset_price else st.sidebar.number_input("Current Asset Price", value=100.0, step=1.00)
        K = st.sidebar.number_input("Strike Price", value=100.0, step=1.00)
        T = st.sidebar.number_input("Time to Maturity (Years)", value=1.0, step=0.25)
        r = st.sidebar.number_input("Risk-Free Interest Rate", value=0.05, step=0.01)
        sigma = st.sidebar.number_input("Volatility (σ)", value=0.2, step=0.1)
        run_button = st.sidebar.button(f"Run {selected_model}")
    
        if run_button:
            st.title(f" {selected_model} Pricing Model")
            if selected_model == "Black-Scholes":
                call_price = black_scholes(S, K, T, r, sigma, "call")
                put_price = black_scholes(S, K, T, r, sigma, "put")
            elif selected_model == "Monte Carlo":
                call_price = monte_carlo(S, K, T, r, sigma, "call")
                put_price = monte_carlo(S, K, T, r, sigma, "put")
            else:
                call_price = binomial_tree(S, K, T, r, sigma, "call")
                put_price = binomial_tree(S, K, T, r, sigma, "put")

            st.markdown("## Option Prices")
            col1, col2 = st.columns(2)
            with col1:
                st.success(f"Call Option Price: ${call_price:.2f}")
            with col2:
                st.error(f"Put Option Price: ${put_price:.2f}")

            # Generate data for call and put options
            stock_prices = np.linspace(S * 0.8, S * 1.2, 20)
            strike_prices = np.linspace(K * 0.8, K * 1.2, 20)
            call_data = np.array([[black_scholes(s, k, T, r, sigma, "call") for k in strike_prices] for s in stock_prices])
            put_data = np.array([[black_scholes(s, k, T, r, sigma, "put") for k in strike_prices] for s in stock_prices])

            # Create interactive heatmap for call options using Plotly
            call_heatmap = go.Figure(data=go.Heatmap(
                z=call_data.tolist(),
                x=strike_prices.tolist(),
                y=stock_prices.tolist(),
                colorscale='Viridis',
                colorbar=dict(title='Call Option Price'),
                zmin=np.min(call_data),
                zmax=np.max(call_data),
                hovertemplate="<b>Stock Price:</b> %{y}<br>" +
                              "<b>Strike Price:</b> %{x}<br>" +
                              "<b>Call Option Price:</b> %{z:.2f}<br>" +
                              "<extra></extra>"
            ))

            # Create interactive heatmap for put options using Plotly
            put_heatmap = go.Figure(data=go.Heatmap(
                z=put_data.tolist(),
                x=strike_prices.tolist(),
                y=stock_prices.tolist(),
                colorscale='Cividis',
                colorbar=dict(title='Put Option Price'),
                zmin=np.min(put_data),
                zmax=np.max(put_data),
                hovertemplate="<b>Stock Price:</b> %{y}<br>" +
                              "<b>Strike Price:</b> %{x}<br>" +
                              "<b>Put Option Price:</b> %{z:.2f}<br>" +
                              "<extra></extra>"
            ))

            st.subheader("Heatmap for Call Options")
            st.plotly_chart(call_heatmap, use_container_width=True)

            st.subheader("Heatmap for Put Options")
            st.plotly_chart(put_heatmap, use_container_width=True)
