import quandl
import pandas as pd


def extract_country_codes():
    country_codes = pd.read_csv('metadata/economist_country_codes.csv', sep = '|')
    return country_codes

def download_data(api_key):
    quandl.ApiConfig.api_key = f'{api_key}'
    data = []
    country_codes = extract_country_codes()
    for index, row in country_codes.iterrows():
        country_code = row['CODE']
        country_name = row['COUNTRY']
        data = quandl.get(f'ECONOMIST/BIGMAC_{country_code}')
        data.insert(0, 'Country', country_name)
        data.to_csv(f'countries_data/{country_code}.csv')

