""" This module is an implementation of FileProcessorInterface """
import sys
import business.constant as constant

from file_source.file_processor import FileProcessorInterface


class CSVFileProcessor(FileProcessorInterface):

    def read_file(self, csv_filename):
        """Read all lines of data from a CSV file"""
        try:
            with open(csv_filename) as file:
                records = file.readlines()
                return [data_record.strip().split(',') for data_record in records]
        except IOError:
            print(f"Incoming file cannot be read:", csv_filename)
            sys.exit()

    def write_file(self, data):
        """Write all lines of data to a CSV file"""
        try:
            with open(constant.OUTPUT_FILE, 'w') as f:
                for record in data:
                    f.write(",".join(record))
                    f.write("\n")
        except IOError:
            print(f"Error writing masked data into a file:")
            sys.exit()
