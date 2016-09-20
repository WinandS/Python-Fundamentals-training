import unittest
import piglatin as p


class TestPiglatin(unittest.TestCase):
    def test_to_piglatin(self):
        words = {"happy" : "appy-hay", "duck" : "uck-day", "glove" : "ove-glay", "egg" : "egg-ay", "inbox" : "inbox-ay", "eight" : "eight-ay"}
        for word, piglatin in words.items():
            self.assertEqual(p.to_piglatin(word), piglatin)

    def test_from_piglatin(self):
        words = {"happy" : "appy-hay", "duck" : "uck-day", "glove" : "ove-glay", "egg" : "egg-ay", "inbox" : "inbox-ay", "eight" : "eight-ay"}
        for word, piglatin in words.items():
            self.assertEqual(p.from_piglatin(piglatin), word)


unittest.main()