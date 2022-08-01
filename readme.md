# Customer Data Processor 

Python application takes a CSV file containing customer data and processes it to produce another CSV file which contains
sensitive data in a masked format. Also, value of billing average is replaced as billing data for all customers. 

In addition, this application also generates a report containing,
#### 1. min, max and average billing value
#### 2. min, max and average length of characters in name values


## To run the application

Sample customers.csv file is available in test_data folder.
Input File Name: customers.csv
```
python3 /CustomerDataProcessor/main.py /customers.csv
```

## Sample output generated

Sample output masked file generated is available in test_data folder for reference.
Output File Name: masked_clients.csv
```
Name of the file passed : /users/dc/documents/neosalpha/vodafone/pythontest/customers.csv
Billing: Max.  60.0 , Min.  60.0 , Avg. 60.0
Name: Max.  7 , Min.  3 , Avg. 5.33
```