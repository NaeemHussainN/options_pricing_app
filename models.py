import numpy as np
from scipy.stats import norm

# ----- Option Pricing Models -----
def black_scholes(S, K, T, r, sigma, option_type="call"):
    """Calculate European option price using the Black-Scholes model."""
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    if option_type == "call":
        return S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    else:
        return K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)

def monte_carlo(S, K, T, r, sigma, option_type="call", num_simulations=10000):
    """Calculate option price using the Monte Carlo method."""
    np.random.seed(0)
    dt = T / 252  # Daily time steps
    simulations = np.zeros(num_simulations)
    for i in range(num_simulations):
        prices = [S]
        for _ in range(int(T / dt)):
            prices.append(prices[-1] * np.exp((r - 0.5 * sigma ** 2) * dt + sigma * np.sqrt(dt) * np.random.normal()))
        final_price = prices[-1]
        if option_type == "call":
            simulations[i] = max(final_price - K, 0)
        else:
            simulations[i] = max(K - final_price, 0)
    return np.exp(-r * T) * np.mean(simulations)

def binomial_tree(S, K, T, r, sigma, option_type="call", num_steps=100):
    """Calculate option price using the Binomial Tree model."""
    dt = T / num_steps  # Time step per iteration
    u = np.exp(sigma * np.sqrt(dt))  # Up factor
    d = 1 / u  # Down factor (inverse of up factor)
    p = (np.exp(r * dt) - d) / (u - d)  # Risk-neutral probability
    discount = np.exp(-r * dt)  # Discount factor per step
    
    # Initialize a 2D array to hold option values at each step
    option_values = np.zeros((num_steps + 1, num_steps + 1))
    
    # Step 1: Calculate option values at maturity (at time T)
    for i in range(num_steps + 1):
        stock_price_at_T = S * (u ** (num_steps - i)) * (d ** i)  # Stock price at maturity
        if option_type == "call":
            option_values[i, num_steps] = max(stock_price_at_T - K, 0)  # Call option payoff
        else:
            option_values[i, num_steps] = max(K - stock_price_at_T, 0)  # Put option payoff
    
    # Step 2: Work backwards through the tree to get the option value at time 0
    for i in range(num_steps - 1, -1, -1):  # Loop backward from maturity
        for j in range(i + 1):  # Loop through each node at this step
            stock_price_at_t = S * (u ** (i - j)) * (d ** j)  # Stock price at time t
            # Calculate the option value at this node (taking risk-neutral expectation)
            if option_type == "call":
                option_values[j, i] = discount * (p * option_values[j, i + 1] + (1 - p) * option_values[j + 1, i + 1])
            else:
                option_values[j, i] = discount * (p * option_values[j, i + 1] + (1 - p) * option_values[j + 1, i + 1])
    
    return option_values[0, 0]  # Return the option value at time 0 (root of the tree)
