import os
import requests

# Urls and filenames of desired data sources
urls = {
    "hydro chem and water": "https://www.aer.ca/documents/by-topic/hydraulic-fracturing/SummaryChemical-WaterUse.csv",
    "hydro water source": "https://www.aer.ca/documents/by-topic/hydraulic-fracturing/WaterSourceData.csv"
    }

filenames = {"hydro chem and water": "SummaryChemical-WaterUse.csv",
             "hydro water source": "WaterSourceData.csv"
             }

# print(urls["hydro chem and water"])

headers = {"User-Agent": "Mozilla/5.0"}
root_path = os.path.abspath(".")
data_path = f"{root_path}/data/raw/"


def get_frac_fluid_data():
    for key, url in urls.items():
        os.makedirs(f"{data_path}", exist_ok=True)
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            with open(f"{data_path}{filenames[key]}", "w", encoding='utf-8') as f:
                f.write(response.text)
            print(f"Download of {filenames[key]} Successful")
        else:
            print(f"Failed to download {filenames[key]}: {response.status_code}")

# print(data_path)