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


## Parameters
- **Asset Price (S):** Current price of the underlying asset.
- **Strike Price (K):** Price at which the option can be exercised.
- **Time to Maturity (T):** The time left until expiration (years).
- **Risk-Free Rate (r):** Annual risk-free interest rate.
- **Volatility (σ):** Expected price fluctuation of the asset.
- **Ticker Symbol (optional):** Fetch real-time stock prices.

# Streamlit Web App Demonstrations
Below are demonstrations of each pricing model in action:



## Black-Scholes Pricing Model (1973)
The Black-Scholes Pricing Model, developed by Fischer Black, Myron Scholes, and Robert Merton in 1973, revolutionized the way options are priced in the financial markets. It provided a groundbreaking formula to calculate the theoretical value of European-style options. The model takes into account several factors:

1. **Underlying Asset Price (S)**: The current market price of the underlying asset.
2. **Strike Price (K)**: The predetermined price at which the option holder can buy or sell the underlying asset.
3. **Time to Expiration (T)**: The remaining time until the option's expiration.
4. **Risk-free Interest Rate (r)**: The continuously compounded risk-free interest rate over the option's time to expiration.
5. **Volatility (σ)**: The standard deviation of the underlying asset's returns, indicating the level of its price fluctuations.
Using the Black-Scholes formula, the theoretical value of a European call option (C) and a European put option (P) can be calculated as follows:


**Call Option:**
$$Call = S \cdot N(d1) - K \cdot e^{-r \cdot T} \cdot N(d2)$$

**Put Option:**
$$Put = K \cdot e^{-r \cdot T} \cdot N(-d2) - S \cdot N(-d1)$$

Where:

$$d1 = \frac{\ln\left(\frac{S}{K}\right) + \left(r + \frac{\sigma^2}{2}\right) \cdot T}{\sigma \cdot \sqrt{T}}$$

$$d2 = d1 - \sigma \cdot \sqrt{T}$$


![Black-Scholes](https://github.com/NaeemHussainN/options_pricing_platform/blob/main/black_scholes_model.gif)



## Monte Carlo Simulation for Option Pricing  
Monte Carlo Simulation is a numerical technique used to estimate the theoretical value of financial derivatives, including options. Unlike the Black-Scholes model, which provides a closed-form solution, Monte Carlo methods rely on repeated random sampling to simulate potential future price paths of the underlying asset. This approach is particularly useful for pricing complex options where analytical solutions are not feasible. The model considers several factors:  

1. **Underlying Asset Price (S)**: The current market price of the underlying asset.  
2. **Strike Price (K)**: The predetermined price at which the option holder can buy or sell the underlying asset.  
3. **Time to Expiration (T)**: The remaining time until the option's expiration.  
4. **Risk-free Interest Rate (r)**: The continuously compounded risk-free interest rate over the option's time to expiration.  
5. **Volatility (σ)**: The standard deviation of the underlying asset's returns, indicating the level of its price fluctuations.  
6. **Number of Simulations (N)**: The number of random price paths generated to approximate the option price.  

Using the Monte Carlo method, the theoretical value of a European call option (C) and a European put option (P) can be estimated as follows:  

### Simulating Future Price Paths:  
The underlying asset price follows a **discretized Geometric Brownian Motion** with daily steps:

**Call Option:**  
$$Call = e^{-r \cdot T} \cdot \frac{1}{N} \sum_{i=1}^{N} \max(S_T^i - K, 0)$$  

**Put Option:**  
$$Put = e^{-r \cdot T} \cdot \frac{1}{N} \sum_{i=1}^{N} \max(K - S_T^i, 0)$$  

Where:  

$$S_T = S \cdot e^{\left( r - \frac{1}{2} \sigma^2 \right) \cdot T + \sigma \cdot \sqrt{T} \cdot Z}$$

Here, \( Z \) is a random variable drawn from a standard normal distribution (\( Z \sim N(0,1) \)).

Monte Carlo methods are widely used in quantitative finance due to their flexibility in pricing complex derivatives and handling scenarios where closed-form solutions do not exist.

![Monte Carlo](https://github.com/NaeemHussainN/options_pricing_platform/blob/main/monte_carlo_model.gif)


## Binomial Tree Model for Option Pricing  
The Binomial Tree Model is a numerical method used to estimate the theoretical value of options by discretizing the price movement of the underlying asset over multiple time steps. Unlike the Black-Scholes model, which assumes continuous price movement, the Binomial Tree model constructs a step-by-step evolution of the asset price, making it particularly useful for pricing American-style options that can be exercised before expiration. The model considers several factors:  

1. **Underlying Asset Price (S)**: The current market price of the underlying asset.  
2. **Strike Price (K)**: The predetermined price at which the option holder can buy or sell the underlying asset.  
3. **Time to Expiration (T)**: The remaining time until the option's expiration, divided into \( N \) discrete time steps.  
4. **Risk-free Interest Rate (r)**: The continuously compounded risk-free interest rate over the option's time to expiration.  
5. **Volatility (σ)**: The standard deviation of the underlying asset's returns, indicating the level of its price fluctuations.  
6. **Number of Steps (N)**: The number of discrete time steps used to model the price evolution.  

Using the Binomial Tree method, the theoretical value of a European call option (C) and a European put option (P) can be estimated as follows:  

### **Upward and Downward Price Movements:**  
The asset price moves up or down at each time step based on a binomial process:  

$$ u = e^{\sigma \cdot \sqrt{\Delta t}} $$  

$$ d = e^{-\sigma \cdot \sqrt{\Delta t}} $$  

Where \( \Delta t = \frac{T}{N} \) is the length of each time step.  

### **Risk-Neutral Probability:**  
The probability of an upward movement in a risk-neutral world is given by:  

$$ p = \frac{e^{r \cdot \Delta t} - d}{u - d} $$  

### **Call Option:**  
$$ Call = e^{-r \cdot T} \sum_{i=0}^{N} \binom{N}{i} p^i (1 - p)^{N-i} \max(S \cdot u^i \cdot d^{N-i} - K, 0) $$  

### **Put Option:**  
$$ Put = e^{-r \cdot T} \sum_{i=0}^{N} \binom{N}{i} p^i (1 - p)^{N-i} \max(K - S \cdot u^i \cdot d^{N-i}, 0) $$  

Where:  

- \( u \) and \( d \) are the up and down factors for price movement.  
- \( p \) is the risk-neutral probability.  





The Binomial Tree model is widely used in quantitative finance due to its ability to price both European and American options, incorporate early exercise features, and handle various dividend structures.  

![Binomial Tree](https://your-image-url.com/binomial_tree.gif)



## Dependencies
- **Streamlit** (for UI)
- **Yahoo Finance (yfinance)** (for fetching stock prices)
- **NumPy** (for calculations)
- **Plotly** (for visualization)

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



