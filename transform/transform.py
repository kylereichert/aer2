# %%
import os
import pandas as pd
from db.connection import create_table

root = os.path.abspath("..")
raw_data_path = f"{root}/data/raw"


# %%
data = pd.read_csv(f"{raw_data_path}/SummaryChemical-WaterUse.csv", sep='|')

#%%
# create_table(data, "summary_chemical_wateruse")
# %%
