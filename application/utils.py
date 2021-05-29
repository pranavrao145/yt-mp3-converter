import requests
import os

def getSearches(query):
    url = f"https://youtube.googleapis.com/youtube/v3/search?part=snippet&q={query.lower()}&maxResults=10&key={os.environ.get('YOUTUBE_API_TOKEN')}" 
    response = requests.get(url).json()
    return response["items"]

def getChannelName(channelID):
    url = f"https://www.googleapis.com/youtube/v3/channels?part=snippet&id={channelID}&key={os.environ.get('YOUTUBE_API_TOKEN')}" 
    response = requests.get(url).json()
    print(type(response))
    return response["items"][0]["snippet"]["title"]
