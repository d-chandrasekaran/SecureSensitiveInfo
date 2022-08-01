import os
import sys

from file_source.csv_file_processor import CSVFileProcessor as CSVFileProcessor
from validator.data_validator import DataValidator as DataValidator
from business.customer_data_processor import CustomerDataProcessor


def secure_csv_file(csv_filename):
    """Method to orchestrate load, validate, mask, write customer records"""

    csv_file_processor = CSVFileProcessor()
    customer_data = csv_file_processor.read_file(csv_filename)

    DataValidator.validate_data(customer_data)

    processor = CustomerDataProcessor(customer_data)
    masked_customer_data = processor.execute()
    csv_file_processor.write_file(masked_customer_data)


try:
    file_name = sys.argv[1].lower()
    print(f'Name of the file passed : {file_name}')
    file_type = os.path.splitext(file_name)
    if file_type[1] == ".csv":
        secure_csv_file(file_name)
    else:
        print('Sorry, provided file type is currently not supported')
except IndexError:
    print("No file passed for processing")
    sys.exit()
