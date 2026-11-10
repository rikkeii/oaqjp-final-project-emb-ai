# Final project

AI-based web application that performs emotion detection on customer feedback
using the embeddable Watson NLP library (EmotionPredict).

## Structure

```
final_project/
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
├── static/
│   └── mywebscript.js
├── templates/
│   └── index.html
├── server.py
├── test_emotion_detection.py
└── README.md
```

## Run

```bash
python3 -m pip install requests flask
python3 server.py          # serves the app on http://localhost:5000
python3 test_emotion_detection.py   # run unit tests
```

The Watson NLP endpoint is only reachable from the Skills Network Theia Lab environment.
S
