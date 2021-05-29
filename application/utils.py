import requests
import os
import urllib.parse

def getSearches(query):
    url = f"https://youtube.googleapis.com/youtube/v3/search?part=snippet&q={urllib.parse.quote(query.lower())}&maxResults=10&key={os.environ.get('YOUTUBE_API_TOKEN')}" 
    print(url)
    response = requests.get(url).json()
    return response["items"]

