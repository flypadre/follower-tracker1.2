import unittest
from x_api import get_mutual_followers

class TextXApi(unittest.TestCase):
    def test_get_mutual_followers(self):
        # Mock API response or use a test account
        result = get_mutual_followers()
        self.assertIsInstance(result, list)

if __name__ == '__main__':
    unittest.main()