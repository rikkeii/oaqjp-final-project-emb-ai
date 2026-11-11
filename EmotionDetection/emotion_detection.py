"""Emotion detection application built on the Watson NLP EmotionPredict function."""

import json

import requests

URL = (
    "https://sn-watson-emotion.labs.skills.network/v1/"
    "watson.runtime.nlp.v1/NlpService/EmotionPredict"
)
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
EMOTIONS = ("anger", "disgust", "fear", "joy", "sadness")


def emotion_detector(text_to_analyze):
    """Analyze the emotions expressed in a piece of text.

    Args:
        text_to_analyze: The text whose emotions should be detected.

    Returns:
        A dictionary with the scores for anger, disgust, fear, joy and sadness,
        plus the key 'dominant_emotion' naming the highest-scoring emotion.
        If the server rejects the request (status code 400, e.g. blank input),
        every value in the dictionary is None.
    """
    payload = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(URL, json=payload, headers=HEADERS, timeout=30)

    if response.status_code == 400:
        result = {emotion: None for emotion in EMOTIONS}
        result["dominant_emotion"] = None
        return result

    response_dict = json.loads(response.text)
    scores = response_dict["emotionPredictions"][0]["emotion"]

    result = {emotion: scores[emotion] for emotion in EMOTIONS}
    result["dominant_emotion"] = max(EMOTIONS, key=lambda emotion: result[emotion])
    return result
