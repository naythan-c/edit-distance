import unittest
import edit_distance

class TestEditDistance(unittest.TestCase):

    def test_edit_distance(self):
        result = edit_distance.edit_distance("cat", "bag")
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()