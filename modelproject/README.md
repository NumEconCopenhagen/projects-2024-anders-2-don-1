# Model analysis project

Our project is titled **Dynamic GARCH portfolio and utility optimization**. We extend the methods and results from the Data project by engaging the portfolio optimization problem using GARCH-modeling and assuming that the investor can exploit new information each period to reallocate his/her assets. From this, we find that the Sharpe-ratio (risk-adjusted return) can be increased relative to the benchmark portfolio (which represents the portfolio derived from the Data project assuming constant volatility over time). We further extend the Capital Asset Pricing model by assuming specific investor preferences and parameters for risk aversion to find a closed solution to the dilemma proposed by CAPM: how much to actually divide ones capital between risky and safe assets.

The **results** of the project can be seen from running [modelproject.ipynb](modelproject.ipynb).

**Dependencies:** Apart from a standard Anaconda Python 3 installation, the project requires the following installations:

``pip install pandas``
``pip install numpy``
``pip install matplotlib.pyplot``
``pip install arch``

