""" This module contains operations to be performed on customer data """
import sys
import business.constant as constant


class CustomerDataProcessor:

    def __init__(self, data):
        """__init__ constructor class for CustomerDataProcessor"""

        self.data = data

    def compute_billing_avg(self):
        """Method computes the average of data values contained in BILLING column"""

        billing_records = [customer_record[constant.BILLING] for customer_record in self.data[1:]]
        try:
            billing_records = [0 if billing_item == '' else float(billing_item) for billing_item in billing_records]
            billing_average = sum(billing_records) / len(billing_records)
            print("Billing: Max. ", max(billing_records), ", Min. ", min(billing_records), ", Avg.",
                  str(round(billing_average, 2)))
            return str(round(billing_average, 2))
        except ValueError:
            print(f"Billing data contains non-numeric value")
            sys.exit()

    def update_customer_billing(self, billing_average):
        """Method updates billing value with the average of data values contained in BILLING column"""

        for customer_record in self.data[1:]:
            customer_record[constant.BILLING] = billing_average

    def compute_name_aggregate(self):
        """Method computes the aggregate (min, max and average) length of data contained in NAME column"""

        name_records = [customer_record[constant.NAME] for customer_record in self.data[1:]]
        max_len_name = len(max(name_records, key=len))
        min_len_name = len(min(name_records, key=len))
        avg_len_name = sum(map(len, name_records)) / float(len(name_records))
        print("Name: Max. ", max_len_name, ", Min. ", min_len_name, ", Avg.", str(round(avg_len_name, 2)))

    @staticmethod
    def mask(sensitive_data):
        """Method to mask sensitive alpha characters"""

        return "".join([constant.MASK if character.isalpha() else character for character in sensitive_data])

    def mask_sensitive_data(self):
        """Method to mask data in NAME and EMAIL column"""

        for customer_record in self.data[1:]:
            customer_record[constant.NAME] = self.mask(customer_record[constant.NAME])
            customer_record[constant.EMAIL] = self.mask(customer_record[constant.EMAIL])

    def execute(self):
        """Method to orchestrate the business logic"""

        average = self.compute_billing_avg()
        self.update_customer_billing(average)
        self.compute_name_aggregate()
        self.mask_sensitive_data()
        return self.data
