import requests
from bs4 import BeautifulSoup
import re
import time

# Open the file and read the lines
with open('input.txt', 'r') as file:
    lines = file.readlines()

# Loop through each line in the file
for line in lines:
    # Remove any newline characters from the line
    number = line.strip()

    # Insert the number into the URL
    url = f'https://engineering.teads.com/sustainability/carbon-footprint-estimator-for-aws-instances/?estimation=true&instance_id={number}&region_id=2232&compute_hours=24#calculator'

    response = requests.get(url)

    # Print the response status code
    print(response.status_code)

    # Parse the response content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Define a pattern that starts with "Just estimated the carbon footprint"
    pattern = r"Just estimated the carbon footprint[^\n]*"

    # Search for the pattern in the parsed HTML content
    match = re.search(pattern, str(soup))

    if match:
        # If a match is found, print the matched string
        print(match.group())
        # Append the matched string to a file named response.txt
        with open('response.txt', 'a') as f:
            f.write(match.group() + '\n')
    else:
        # If no match is found, print a suitable message
        print("No match found")

    # Delay for 3 seconds
    time.sleep(3)
