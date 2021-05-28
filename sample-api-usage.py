import requests

def getSearches(query):
   print("hello, this function was indeed called")
   url = f"https://youtube.googleapis.com/youtube/v3/search?part=snippet&q={query.lower()}&key=AIzaSyDxgY7C4_-vWR47yz1-IegEEBzis4ZF76E" 
   response = requests.get(url).json()
   return response

if __name__ == "__main__":
    print(getSearches("mozart"))

