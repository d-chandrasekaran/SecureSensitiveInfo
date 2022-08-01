import business.constant as constant
import sys


class DataValidator:

    @staticmethod
    def validate_data(customer_data):
        """Method to validate the CSV file and header record"""

        if len(customer_data) >= 2:
            header_record = [header_element.upper() for header_element in customer_data[0]]
            master_list = ['ID', 'NAME', 'EMAIL', 'BILLING', 'LOCATION']
            if header_record != master_list:
                print("Incoming CSV file has malformed header")
                sys.exit()
        else:
            print(f"No records are available in the file or file is malformed")
            sys.exit()
