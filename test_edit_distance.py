import unittest
import edit_distance

class TestEditDistance(unittest.TestCase):

    def test_edit_distance(self):
        #Valid Data
        self.assertEqual(edit_distance.edit_distance("snowy", "sunny"), 3)

        #Borderline Data
        self.assertEqual(edit_distance.edit_distance("", ""), 0)
        self.assertEqual(edit_distance.edit_distance("", "exponential"), 11)
        self.assertEqual(edit_distance.edit_distance("polynomial", ""), 10)

        # # #Errornous Data
        # self.assertRaises(ValueError, edit_distance.edit_distance, "cAt", "bag")
        # self.assertRaises(ValueError, edit_distance.edit_distance, "cat", "bAg")
        # self.assertRaises(ValueError, edit_distance.edit_distance, "cAt", "bAg")

        #Out of bounds Data

if __name__ == '__main__':
    unittest.main()