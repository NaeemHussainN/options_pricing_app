# Options Pricing Platform

## Overview
This project is a **Streamlit-based Options Pricing Platform** that allows users to calculate **call** and **put** option prices using three different pricing models:

1. **Black-Scholes Model** (for European options)
2. **Monte Carlo Simulation**
3. **Binomial Tree Model**

The application provides an intuitive **UI with interactive heatmaps** to visualize option price variations based on asset and strike prices.

## Features
- Retrieve real-time asset prices using **Yahoo Finance**.
- Select between **Black-Scholes, Monte Carlo, or Binomial Tree models**.
- Enter **custom parameters** for asset price, strike price, volatility, interest rate, and maturity.
- **Heatmaps** to visualize pricing behavior under different conditions.
- **GIF Demonstrations** of each pricing model in action.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/NaeemHussainN/options-pricing-platform.git
    cd options-pricing-platform
    ```

2. Create a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
Run the application with the following command:

```bash
streamlit run app.py
```

## Parameters
- **Asset Price (S):** Current price of the underlying asset.
- **Strike Price (K):** Price at which the option can be exercised.
- **Time to Maturity (T):** The time left until expiration (years).
- **Risk-Free Rate (r):** Annual risk-free interest rate.
- **Volatility (σ):** Expected price fluctuation of the asset.
- **Ticker Symbol (optional):** Fetch real-time stock prices.

# Streamlit Web App Demonstrations
Below are demonstrations of each pricing model in action:


## Black-Scholes Model

![Black-Scholes](https://github.com/NaeemHussainN/options_pricing_platform/blob/main/black_scholes.gif)

The Black-Scholes model is used to price European options. It assumes a lognormal distribution of stock prices and provides a closed-form solution for option pricing.

## Monte Carlo Simulation

![Monte Carlo](https://your-image-url.com/monte_carlo.gif)

Monte Carlo simulation estimates option prices by simulating multiple possible paths for the underlying asset and averaging the discounted payoffs.

## Binomial Tree Model

![Binomial Tree](https://your-image-url.com/binomial_tree.gif)

The Binomial model prices options by constructing a recombining price tree over multiple periods and working backwards to determine option value.

## Dependencies
- **Streamlit** (for UI)
- **Yahoo Finance (yfinance)** (for fetching stock prices)
- **NumPy** (for calculations)
- **Plotly** (for visualization)

Install them using:
```bash
pip install -r requirements.txt
```

## File Structure
```
options-pricing-platform/
│── app.py                 # Main application script
│── models.py              # Contains Black-Scholes, Monte Carlo, and Binomial Tree implementations
│── requirements.txt       # Dependencies
│── README.md              # Project documentation
```

## Contributing
Pull requests are welcome! If you'd like to add features or improve existing code, feel free to fork the repository and submit a PR.

## License
This project is licensed under the **MIT License**.

