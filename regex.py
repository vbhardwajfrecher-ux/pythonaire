import re

enter_paragraph = input("Enter Paragraph: ")
find_word = input("Find replacement word: ")
Enter_replacement = input("Enter the replacement: ")

string = enter_paragraph
pattern = find_word
replacement = Enter_replacement

result = re.sub(pattern, replacement, string)
print(result)

"""
@problem :-By API fetching data with data validation who's initial starts with FNB, ZXX and PPO
           through reguler expression 


Description:-

Send a request to the API to retrieve the data.

Validate the data using regular expressions that match patterns starting with "FNB", "ZXX", or "PPO".

Filter out any data that does not match these patterns.

Here's an example Python code snippet that fetches data from an API and validates it
based on the required patterns using regular expressions:
"""

import re
import requests

# URL of the API
url = "https://api.example.com/data"

# Send a GET request to the API
response = requests.get(url)

# Check if the response was successful
if response.status_code == 200:
    # Extract the data from the response
    data = response.json()

    # Define the regular expression patterns
    pattern1 = "^FNB.*"
    pattern2 = "^ZXX.*"
    pattern3 = "^PPO.*"

    # Validate the data using the regular expressions
    filtered_data = []
    for d in data:
        if re.match(pattern1, d) or re.match(pattern2, d) or re.match(pattern3, d):
            filtered_data.append(d)

    # Use the filtered data as required
    print(filtered_data)

else:
    # Handle the error
    print("Error fetching data from API")
    
    
#The regular expression patterns are defined using the "^" character, 
#which means the pattern must match the start of the string. 
#The ".*" characters at the end of each pattern indicate that the pattern can be followed by any number of characters.
#The code uses the Python "re" module to perform the regular expression matching. 
#The filtered data is stored in a new list called "filtered_data", which can be used as required.



