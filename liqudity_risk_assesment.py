import pandas as pd
import numpy as np
import plotly.graph_objects as go

# Step 1: Generate synthetic portfolio data
np.random.seed(42)
n_assets = 50
df = pd.DataFrame({
    'asset_id': [f'A{i}' for i in range(n_assets)],
    'value': np.random.uniform(100000, 1000000, n_assets),  # Asset values in USD
    'liquidity_score': np.random.uniform(0.2, 1.0, n_assets),  # 1.0 = highly liquid
    'market_volatility': np.random.uniform(0.05, 0.3, n_assets)  # Volatility factor
})

# Step 2: Define liquidity cost function
def calc_liquidation_cost(val, liq_score, vol, stress_factor=1.0):
    base_cost = val * (1 - liq_score) * vol  # Cost increases with lower liquidity
    return base_cost * stress_factor

# Step 3: Simulate liquidation under normal and stressed conditions
df['normal_cost'] = df.apply(
    lambda row: calc_liquidation_cost(row['value'], row['liquidity_score'], row['market_volatility']), axis=1
)
df['stress_cost'] = df.apply(
    lambda row: calc_liquidation_cost(row['value'], row['liquidity_score'], row['market_volatility'], 1.5), axis=1
)

# Step 4: Estimate liquidation time (days) based on liquidity score
df['normal_time'] = (1 - df['liquidity_score']) * 30  # Max 30 days for illiquid assets
df['stress_time'] = df['normal_time'] * 1.2  # 20% longer in stressed conditions

# Step 5: Aggregate portfolio metrics
total_value = df['value'].sum()
normal_liq_cost = df['normal_cost'].sum() / total_value * 100  # % of portfolio value
stress_liq_cost = df['stress_cost'].sum() / total_value * 100
avg_normal_time = df['normal_time'].mean()
avg_stress_time = df['stress_time'].mean()

# Step 6: Prepare data for plotting
X = df['asset_id']
Y_normal = df['normal_cost'] / df['value'] * 100  # % cost per asset
Y_stress = df['stress_cost'] / df['value'] * 100

# Step 7: Create Plotly visualization
fig = go.Figure()
fig.add_trace(go.Scatter(
    x=X, y=Y_normal, mode='lines', name='Normal Conditions',
    line=dict(color='#FF6B6B', width=2)  # Reddish for actual data
))
fig.add_trace(go.Scatter(
    x=X, y=Y_stress, mode='lines', name='Stressed Conditions',
    line=dict(color='#4ECDC4', width=2, dash='dash')  # Teal dashed for stressed
))

# Apply dark theme and styling
fig.update_layout(
    title='Liquidity Cost per Asset (% of Value)',
    xaxis_title='Asset ID',
    yaxis_title='Liquidation Cost (%)',
    plot_bgcolor='rgb(40, 40, 40)',
    paper_bgcolor='rgb(40, 40, 40)',
    font=dict(color='white'),
    xaxis=dict(gridcolor='rgba(255, 255, 255, 0.1)', gridwidth=0.5),
    yaxis=dict(gridcolor='rgba(255, 255, 255, 0.1)', gridwidth=0.5),
    margin=dict(l=50, r=50, t=50, b=50),
    showlegend=True
)

# Step 8: Display results
print(f"Portfolio Value: ${total_value:,.2f}")
print(f"Normal Conditions - Liquidity Cost: {normal_liq_cost:.2f}% | Avg Time: {avg_normal_time:.1f} days")
print(f"Stressed Conditions - Liquidity Cost: {stress_liq_cost:.2f}% | Avg Time: {avg_stress_time:.1f} days")
fig.show()
