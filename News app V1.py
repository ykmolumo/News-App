import requests
import json

# Insert your own API key here
api_key = "22316a3aad8b4fccae85cb44a90ec513"

# Specify the news source and sort type
source = "bbc-news"
sort_by = "top"

# Make the API request
url = f"https://newsapi.org/v2/top-headlines?sources={source}&sortBy={sort_by}&apiKey={api_key}"
response = requests.get(url)

# Parse the JSON response
data = json.loads(response.text)

# Print the article titles
for article in data["articles"]:
    print(article["title"])
