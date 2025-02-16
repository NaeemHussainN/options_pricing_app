import streamlit as st
import numpy as np
import yfinance as yf
import plotly.graph_objects as go
from models import black_scholes, monte_carlo, binomial_tree  # Import models

st.set_page_config(page_title="Options Pricing Platform", layout="wide")

# Session State for Intro Page
if 'started' not in st.session_state:
    st.session_state.started = False

if not st.session_state.started:
    st.title("Welcome to the Options Pricing Platform!")
    st.markdown("""
    ### Instructions:
    This tool allows you to price **European call & put options** using:
    - **Black-Scholes Model**
    - **Monte Carlo Simulation**
    - **Binomial Tree Model**
    
    Click 'Get Started' to proceed.
    """)
    if st.button("Get Started"):
        st.session_state.started = True

if st.session_state.started:
    st.sidebar.markdown("# Options Pricing Platform")

    # Model selection
    selected_model = st.sidebar.radio("Select an Option Pricing Model", ["Black-Scholes", "Monte Carlo", "Binomial Tree"])

    # Ticker input
    ticker = st.sidebar.text_input("Enter Ticker Symbol (or N/A)", "N/A")
    asset_price = None
    if ticker.upper() != "N/A":
        try:
            asset_price = yf.Ticker(ticker).history(period="1d")["Close"].iloc[-1]
            st.sidebar.success(f"Ticker Price: ${asset_price:.2f}")
        except:
            st.sidebar.error("Invalid ticker symbol. Using manual input.")

    # Input fields
    S = asset_price if asset_price else st.sidebar.number_input("Current Asset Price", value=100.0, step=1.00)
    K = st.sidebar.number_input("Strike Price", value=100.0, step=1.00)
    T = st.sidebar.number_input("Time to Maturity (Years)", value=1.0, step=0.25)
    r = st.sidebar.number_input("Risk-Free Interest Rate", value=0.05, step=0.01)
    sigma = st.sidebar.number_input("Volatility (σ)", value=0.2, step=0.1)
    
    if st.sidebar.button(f"Run {selected_model}"):
        st.title(f"{selected_model} Pricing Model")
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

