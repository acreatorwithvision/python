import requests

# api key and url
api_key="04025c7256c64b828a3c119b9c96888c"
url = "https://newsapi.org/v2/everything?q=tesla&from=2024-09-08&sortBy=publishedAt&apiKey=04025c7256c64b828a3c119b9c96888c"

# make a request
request = requests.get(url)

# get a dictionary with data
content = request.json()

# access the list of titles
for article in content["articles"]:
    print(article["title"])