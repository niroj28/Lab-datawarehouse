
import csv
import pandas as pd
from datetime import datetime

# Open the input and output CSV files
with open('people.csv') as input_file, open('people_with_age.csv', 'w', newline='') as output_file:
    csv_reader = csv.DictReader(input_file)
    fieldnames = ['ID', 'Name', 'DateOfBirth' , 'Salary' ,'Age']
    csv_writer = csv.DictWriter(output_file, fieldnames=fieldnames)
    csv_writer.writeheader()

    # Loop through each row in the CSV file
    for row in csv_reader:
        # Get the date of birth from the row
        dob = datetime.strptime(row['DateOfBirth'], '%m/%d/%Y').date()

        # Calculate the age based on the date of birth
        age = (datetime.now().date() - dob).days // 365

        # Add the age to the row
        row['Age'] = age

        # Write the updated row to the output CSV file
        csv_writer.writerow(row)

data = pd.read_csv('people.csv')
print("Original data")
print(data.to_string(index=False))


data1 = pd.read_csv('people_with_age.csv')
print("\nTransformed Data")
print(data1.to_string(index=False))
