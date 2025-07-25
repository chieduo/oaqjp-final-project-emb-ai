from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        # Test that joy is the dominant emotion
        test_statement_1 = emotion_detector('I am glad this happened')
        self.assertEqual(test_statement_1['dominant_emotion'], 'joy')
        # Test that anger is the dominant emotion
        test_statement_2 = emotion_detector('I am really mad about this	')
        self.assertEqual(test_statement_2['dominant_emotion'], 'anger')
        # Test that disgust is the dominant emotion
        test_statement_3 = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(test_statement_3['dominant_emotion'], 'disgust')
        # Test that sadness is the dominant emotion
        test_statement_4 = emotion_detector('I am so sad about this')
        self.assertEqual(test_statement_4['dominant_emotion'], 'sadness')
        # Test that fear is the dominant emotion
        test_statement_5 = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(test_statement_5['dominant_emotion'], 'fear')

unittest.main()