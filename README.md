# \[Anders^2+Don^1\]

**Group members:**
- Anders Bille
- Anders Halberg
- Julius Mikkelsen

This repository contains  
1. Inaugural project. 
2. Data project. We fetch data from finance.yahoo.com and nasdaqomxnordic.com for the index C25, S&P 500 and DAX. Using this data we can create the efficient tangent portfolio for C25, S&P 500 and DAX using the Capital Asset Pricing Model (CAPM). We show that for a risk free rate of 3% we get that the weights of efficient tangent portfolio is: C25 (68.701468%), S&P(90.569128%) and DAX(-59.270596%) 
3. Model project. We extend the methods and results from the Data project by engaging the portfolio optimization problem using GARCH-modeling and assuming that the investor can exploit new information each period to reallocate his/her assets. From this, we find that the Sharpe-ratio (risk-adjusted return) can be increased relative to the benchmark portfolio (which represents the portfolio derived from the Data project assuming constant volatility over time). We further extend the Capital Asset Pricing model by assuming specific investor preferences and parameters for risk aversion to find a closed solution to the dilemma proposed by CAPM: how much to actually divide ones capital between risky and safe assets.

