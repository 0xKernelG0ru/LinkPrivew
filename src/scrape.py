from apiclient.discovery import build
from apiclient.errors import HttpError
import json
import argparse


DEVELOPER_KEY = "API-KEY"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def find_youtube_data(song):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

  search_response = youtube.search().list(
    q=song,
    part="snippet",
    maxResults=1
  ).execute()
  
  
  result_set = json.dumps(search_response)
  json_data = json.loads(result_set)
  for song in json_data.get("items"):
    if song["id"]["kind"] == "youtube#video":
      given_json = {'Title':song["snippet"]["title"],'Thumbnail':song["snippet"]['thumbnails']['medium']['url'],
      'Description':song["snippet"]["description"]}
      data = json.dumps(given_json, sort_keys=True,
                         indent=4, separators=(',',':'))
      with open('data.txt', 'a') as outfile:
        outfile.write(data)
		
  
  


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("url", help="Enter a YouTube video URL.")
  args = parser.parse_args()
  args.url.replace('https://www.youtube.com/watch?v=','')
  try:
    find_youtube_data(args.url)
  except HttpError, e:
    print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)
  except UnicodeEncodeError:
    print "A unicode error occured, sorry."
