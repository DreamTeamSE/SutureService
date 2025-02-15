import csv
import requests
from io import StringIO

# Assuming the response content is a raw CSV string
response_text = """0, 2.44, -0.12, 0.49
100, -0.06, -0.49, 0.06
200, 0.79, -0.06, 0.24
300, 1.22, -0.49, 0.49
400, 5.80, 0.98, 1.59"""

# Use StringIO to simulate a file object
csv_file = StringIO(response_text)
reader = csv.reader(csv_file, skipinitialspace=True)

# Iterate over rows
for row in reader:
    print(row)  # Each row will be a list of values
