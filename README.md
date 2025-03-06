# Liquidity Risk Assessment Tool

- This Python tool evaluates the liquidity risk of a portfolio by assessing the cost and time required to liquidate assets under normal and stressed conditions.
- It’s designed to ensure assets (e.g., loans, securitized products) can be liquidated or funded without significant loss, critical for managing diverse portfolios.

---

## Files
- `liquidity_risk_assessment.py`: Main script for generating synthetic portfolio data, calculating liquidity metrics, and visualizing results with Plotly.
- `output.png`: Plot.

---

## Libraries Used
- `pandas`
- `numpy`
- `plotly`

---

## Features
- **Data Generation**: Creates synthetic portfolio data with asset values, liquidity scores (0.2 to 1.0), and market volatility.
- **Liquidity Cost**: Estimates liquidation cost as a function of asset value, liquidity score, volatility, and a stress factor (1.5x in stressed conditions).
- **Liquidation Time**: Calculates days to liquidate based on liquidity score (up to 30 days), with a 20% increase under stress.
- **Portfolio Metrics**: Aggregates total value, percentage liquidity cost, and average liquidation time for normal and stressed scenarios.
- **Visualization**: Plots per-asset liquidation cost (% of value) for both conditions using Plotly.
