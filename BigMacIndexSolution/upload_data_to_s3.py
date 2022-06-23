import boto3
from pprint import pprint
import pathlib
import os

def upload_file_to_s3():
    s3 = boto3.client("s3", 
                aws_access_key_id='',
                aws_secret_access_key='')
    bucket_name = "awsmonikabucket"
    object_name = "countries_data_merged.csv"
    file_name = os.path.join(pathlib.Path(__file__).parent.resolve(), "output_countries_data/countries_data_merged.csv")
    response = s3.upload_file(file_name, bucket_name, object_name)
    pprint(response)  

