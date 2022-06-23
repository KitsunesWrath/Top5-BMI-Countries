import pandas as pd
import glob
import os

def csv_to_one_file():
    files = os.path.join("BigMacIndexSolution\countries_data", "*.csv")
    files = glob.glob(files)
    df = pd.concat(map(pd.read_csv, files), ignore_index=True)
    df.to_csv('BigMacIndexSolution\output_countries_data\countries_data_merged.csv')
