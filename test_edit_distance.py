import unittest
import edit_distance

class TestEditDistance(unittest.TestCase):

    def test_edit_distance(self):
        #Valid Cases 
        self.assertEqual(edit_distance.edit_distance("snowy", "sunny"), 3)
        self.assertEqual(edit_distance.edit_distance("exponential", "polynomial"), 6)

        #Border Cases
        self.assertEqual(edit_distance.edit_distance("a", "aaaaaaaaaaa"), 10)
        self.assertEqual(edit_distance.edit_distance("a", "a"), 0)

        #Erroneous Cases
        self.assertRaises(ValueError, edit_distance.edit_distance, "", "exponetial")
        self.assertRaises(ValueError, edit_distance.edit_distance, "exponetial", "")
        self.assertRaises(ValueError, edit_distance.edit_distance, "", "")


if __name__ == '__main__':
    unittest.main()