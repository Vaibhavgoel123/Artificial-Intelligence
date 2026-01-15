from googleapiclient.discovery import build

API_KEY = "YOUR_API_KEY"

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
