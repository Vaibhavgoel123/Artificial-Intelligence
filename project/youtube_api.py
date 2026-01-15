from googleapiclient.discovery import build
import re

API_KEY = "YOUR_API_KEY"

def extract_video_id(url: str):
    patterns = [
        r"v=([^&]+)",
        r"youtu\.be/([^?]+)",
        r"youtube\.com/embed/([^?]+)"
    ]
    for p in patterns:
        m = re.search(p, url)
        if m:
            return m.group(1)
    return None

def fetch_comments(video_id, max_results=100):
  youtube = build('youtube', 'v3', developerKey=API_KEY)
  comments = []

  req = youtube.commentThreads().list(
    part="snippet",
    videoId=video_id,
    maxResults=max_results
  )
    
  res = req.execute()

  for item in res['items']:
    text = item['snippet']['topLevelComment']['snippet']['textDisplay']
    comments.append(text)
  return comments
