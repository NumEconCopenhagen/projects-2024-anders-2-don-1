import pandas as pd
from arch import arch_model

class GARCH:
    def __init__(self, data):
        self.data = data

    def fit_garch_model(self, series):
        model = arch_model(series, vol='Garch', p=1, q=1, rescale=False)
        fitted_model = model.fit(disp='off')
        return fitted_model

    def estimate(self):
        results = {}
        for column in self.data.columns:
            series = self.data[column].dropna()
            fitted_model = self.fit_garch_model(series)
            results[column] = fitted_model
        return results

    def print_results(self, results):
        for index, model in results.items():
            print(f"GARCH(1,1) Model for {index}")
            print(model.summary())
            print("\n")

    def get_parameter_estimates(self, results):
        estimates = {}
        for index, model in results.items():
            params = model.params
            estimates[index] = params
        estimates_df = pd.DataFrame(estimates).T
        return estimates_df



if __name__ == "__main__":
    print("Success1")
