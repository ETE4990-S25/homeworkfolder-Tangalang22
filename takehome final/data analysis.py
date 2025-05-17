import os
import json
from datetime import datetime
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Directory containing currency subfolders
BASE_DIR = 'currency_data'

# Target base currencies and consistent target currency
BASE_CURRENCIES = ['AUD', 'BND', 'CLP', 'DKK', 'ILS']
TARGET_CURRENCY = 'USD'

# Data storage
exchange_data = {currency: [] for currency in BASE_CURRENCIES}
dates = []

# Traverse directories
for base_currency in BASE_CURRENCIES:
    dir_path = os.path.join(BASE_DIR, base_currency)
    if not os.path.exists(dir_path):
        print(f"Directory for {base_currency} not found, skipping.")
        continue

    for file_name in sorted(os.listdir(dir_path)):
        if not file_name.endswith('.json'):
            continue
        file_path = os.path.join(dir_path, file_name)

        with open(file_path, 'r') as f:
            data = json.load(f)

        # Extract date from filename (format: YYYY-MM-DD_exchange_rates_XXX.json)
        try:
            date_str = file_name.split('_')[0]
            date = datetime.strptime(date_str, "%Y-%m-%d").date()
        except Exception as e:
            print(f"Could not parse date from {file_name}: {e}")
            continue

        # Find exchange rate to USD
        rate = None
        for item in data.get("channel", {}).get("item", []):
            if item.get("targetCurrency") == TARGET_CURRENCY:
                try:
                    rate = float(item["exchangeRate"])
                except (KeyError, ValueError):
                    continue
                break

        if rate is not None:
            exchange_data[base_currency].append((date, rate))

# Create DataFrame
df_dict = {'date': sorted(set(date for pairs in exchange_data.values() for date, _ in pairs))}
df = pd.DataFrame(df_dict)
df.set_index('date', inplace=True)

# Populate exchange rates
for currency, records in exchange_data.items():
    rate_map = {date: rate for date, rate in records}
    df[currency] = df.index.map(rate_map.get)

# Reset index for Seaborn compatibility
df_reset = df.reset_index()

# Melt for Seaborn (long-form data)
df_melted = df_reset.melt(id_vars='date', value_vars=BASE_CURRENCIES,
                          var_name='Currency', value_name='ExchangeRate')

# Plot using Seaborn
sns.set(style='whitegrid')
plt.figure(figsize=(14, 7))
sns.lineplot(data=df_melted, x='date', y='ExchangeRate', hue='Currency', linewidth=2)

plt.title(f'Exchange Rate Trends to {TARGET_CURRENCY}', fontsize=16)
plt.xlabel('Date')
plt.show()

#AUD and BND have a dip in comparison to USD right when the COVID-19 pandemic hit.
#DKK and ILS have retained a similar conversion rate to USD over the last decade and a half.
#AUD had a really high exchange value in 2011.