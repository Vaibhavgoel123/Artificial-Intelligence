#  YouTube Sentiment Analyzer API (RNN + LSTM + Attention)

A production‑ready AI system that fetches YouTube comments, analyzes sentiment using a deep learning model (Bi‑LSTM + Attention), supports batch processing, multilingual input, and exposes everything via a FastAPI backend.

Built for research, learning, and real‑world deployment 🚀

---

## ✨ Features

*  Fetch comments directly from YouTube (YouTube Data API v3)
*  Deep Learning model (Embedding → BiLSTM → Attention → Dense)
*  Batch sentiment prediction
*  Multilingual support (tokenizer based)
*  FastAPI backend with Swagger UI
*  Sentiment distribution output (positive / neutral / negative)
*  Chrome extension ready
*  Google Colab compatible

---

## 🧠 Model Architecture

```
Input Text
   ↓
Tokenizer
   ↓
Embedding Layer
   ↓
Bidirectional LSTM
   ↓
Attention Layer
   ↓
Dense + Softmax
   ↓
Sentiment (Negative / Neutral / Positive)
```

---

## 🛠 Tech Stack

| Component     | Technology          |
| ------------- | ------------------- |
| Language      | Python              |
| Backend       | FastAPI             |
| Deep Learning | TensorFlow / Keras  |
| NLP           | Tokenizer + Padding |
| Model         | BiLSTM + Attention  |
| API Hosting   | Uvicorn + Ngrok     |
| Data Source   | YouTube Data API    |

---

## 🚀 Installation

### 1️⃣ Clone or copy project

```bash
git clone <repo-url>
cd sentiment_project
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install fastapi uvicorn tensorflow google-api-python-client pyngrok
```

---

## 🔑 Setup YouTube API Key

Edit `youtube_api.py`:

```python
YOUTUBE_API_KEY = "YOUR_API_KEY_HERE"
```

Create key from:

[https://console.cloud.google.com/](https://console.cloud.google.com/)

Enable **YouTube Data API v3**

---

## ▶ Run API (Local)

```bash
uvicorn api:app --host 0.0.0.0 --port 8000
```

Open:

```
http://127.0.0.1:8000/docs
```

---

## ☁ Run on Google Colab

```python
from pyngrok import ngrok
import nest_asyncio
import uvicorn

nest_asyncio.apply()

public_url = ngrok.connect(8000)
print(public_url)

uvicorn.run("api:app", host="0.0.0.0", port=8000)
```

---

## 🔗 API Endpoints

### 1️⃣ Batch Sentiment Prediction

`POST /predict_batch`

Request:

```json
{
  "comments": ["I love this", "Bad video", "Okay content"]
}
```

Response:

```json
{
  "results": ["positive", "negative", "neutral"]
}
```

---

### 2️⃣ YouTube Video Analysis

`POST /analyze_youtube`

Request:

```json
{
  "url": "https://www.youtube.com/watch?v=VIDEO_ID",
  "max_comments": 100
}
```

Response:

```json
{
  "video_id": "abc123",
  "total_comments": 100,
  "sentiment_counts": {
    "positive": 40,
    "neutral": 35,
    "negative": 25
  }
}
```

---

##  Output Labels

* 0 → Negative
* 1 → Neutral
* 2 → Positive

---

##  Chrome Extension Integration

This API can be used directly inside a Chrome extension using:

```js
fetch("/analyze_youtube")
```

---

##  Model Training

Model was trained using:

* Tokenizer vocabulary size: 20,000
* Max sequence length: 100
* Categorical crossentropy loss
* Adam optimizer

---

##  Error Handling

* Invalid YouTube URL → returns error
* No comments → handled safely
* Model loading protected with custom Attention layer

---

##  Future Improvements

* Emotion classification
* Sarcasm detection
* Transformer model upgrade
* Frontend dashboard
* Database logging
* Docker deployment

---

##  Author

**Vaibhav Goel**

AI and Data Science student

---


