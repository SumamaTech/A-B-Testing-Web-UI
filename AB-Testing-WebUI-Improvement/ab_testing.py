import pandas as pd
import numpy as np
from statsmodels.stats.proportion import proportions_ztest

np.random.seed(42)

n_visitors = 10000
groups = np.random.choice(['A', 'B'], size=n_visitors)

conversion_rates = {'A': 0.10, 'B': 0.12}
converted = [1 if np.random.rand() < conversion_rates[group] else 0 for group in groups]

df = pd.DataFrame({
    'Visitor_ID': range(1, n_visitors + 1),
    'Group': groups,
    'Converted': converted
})

df.to_csv('ab_test_data.csv', index=False)

conversions = df.groupby('Group')['Converted'].sum()
totals = df.groupby('Group')['Converted'].count()

z_stat, p_value = proportions_ztest(count=conversions, nobs=totals)

print(f"Z-statistic: {z_stat:.4f}")
print(f"P-value: {p_value:.4f}")

if p_value < 0.05:
    print("Statistically significant difference found between Group A and B.")
else:
    print("No statistically significant difference between Group A and B.")
