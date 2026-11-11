"""Unit tests for the EmotionDetection package."""
 
import unittest
 
from EmotionDetection.emotion_detection import emotion_detector
 
 
class TestEmotionDetector(unittest.TestCase):
    """Check the dominant emotion returned for each sample statement."""
 
    def test_joy(self):
        """A glad statement should have joy as the dominant emotion."""
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result["dominant_emotion"], "joy")
 
    def test_anger(self):
        """A mad statement should have anger as the dominant emotion."""
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result["dominant_emotion"], "anger")
 
    def test_disgust(self):
        """A disgusted statement should have disgust as the dominant emotion."""
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result["dominant_emotion"], "disgust")
 
    def test_sadness(self):
        """A sad statement should have sadness as the dominant emotion."""
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result["dominant_emotion"], "sadness")
 
    def test_fear(self):
        """An afraid statement should have fear as the dominant emotion."""
        result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result["dominant_emotion"], "fear")
 
 
if __name__ == "__main__":
    unittest.main()