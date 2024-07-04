import json

import requests

# Send a GET using the URL http://127.0.0.1:8000
r = "http://127.0.0.1:8000"
response = requests.get(r)

# Print the status code
print("Status Code: ", response.status_code)
# Print the welcome message
print("Welcome Message: ", response.json())


data = {
    "age": 37,
    "workclass": "Private",
    "fnlgt": 178356,
    "education": "HS-grad",
    "education-num": 10,
    "marital-status": "Married-civ-spouse",
    "occupation": "Prof-specialty",
    "relationship": "Husband",
    "race": "White",
    "sex": "Male",
    "capital-gain": 0,
    "capital-loss": 0,
    "hours-per-week": 40,
    "native-country": "United-States",
}

# Send a POST using the data above
r = "http://127.0.0.1:8000/data/"
post_response = requests.post(r, json=data)

# Print the status code
print("Status Code: ", response.status_code)
# Print the result
print("Result: ", post_response.json())
