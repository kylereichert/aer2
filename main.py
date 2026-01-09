import os
import pandas as pd
from db.connection import connection_test, create_table
from downloader.data import get_frac_fluid_data

root = os.path.abspath(".")
raw_data_path = f"{root}/data/raw"

#print(connection_test())

# get_frac_fluid_data()

df = pd.read_csv(f"{raw_data_path}/SummaryChemical-WaterUse.csv", sep='|')

create_table(df, "summarychemical_wateruse")