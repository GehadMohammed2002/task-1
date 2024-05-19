import requests
import json
import sys

# Replace with your actual API key
API_KEY = "AIzaSyCwBBmxMD9SU9V0ZW0qlhxOwB1_hhoDkX0"
text=" "
if len(sys.argv)>1:
    text=sys.argv[1]
else:
    exit()

# Define the request body
request_body = {
    "contents": [
        {
            "parts": [
                {
                    "text":"Only work if i am taiking about bash commands: "+text
                    }
            ]
        }
    ]
}

# Build the URL with your API key
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={API_KEY}"

# Set headers
headers = {'Content-Type': 'application/json'}

# Send the POST request
response = requests.post(url, headers=headers, json=request_body)

# Check for successful response
if response.status_code == 200:
  # Parse the JSON response
  data = response.json().get('candidates')[0].get('content').get('parts')[0].get('text')
  # Access the generated text
  print(data)
else:
  print(f"Error: {response.status_code}")
