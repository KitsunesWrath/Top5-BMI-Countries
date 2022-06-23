from download_data import download_data
from csv_to_one_file import csv_to_one_file
from upload_data_to_s3 import upload_file_to_s3
from send_email import send_email

email_sender = ""
email_receiver = ""
email_password = ""

api_key = ""

def main():
    download_data(api_key)
    csv_to_one_file()
    upload_file_to_s3()
    send_email(email_sender, email_receiver, email_password)

if __name__ == "__main__":
    main()
