# %%
import os
import pandas as pd

root = os.path.abspath("..")
raw_data_path = f"{root}/data/raw"

# %%
data = pd.read_csv(f"{raw_data_path}/SummaryChemical-WaterUse.csv", sep='|')

# %%
print(data.iloc[1])
# %%
print(data.columns.tolist())
# %%
