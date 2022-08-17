import unittest
import edit_distance


class TestEditDistance(unittest.TestCase):

    # Unit Tests for Edit Distance with Only Insertions, Deletions, and Substitutions
    def test_edit_distance(self):
        # Valid Cases
        self.assertEqual(edit_distance.edit_distance(
            "snowy", "sunny"), 3)  # tests valid words
        self.assertEqual(edit_distance.edit_distance(
            "exponential", "polynomial"), 6)  # tests valid words

        # Boundary Cases
        # tests if there's only one character for word1
        self.assertEqual(edit_distance.edit_distance("a", "aaaaaaaaaaa"), 10)
        # tests if both words are the same
        self.assertEqual(edit_distance.edit_distance("a", "a"), 0)
        # tests strings with numbers
        self.assertEqual(edit_distance.edit_distance(
            "1", "123"), 2)  

        # Erroneous Cases
        # makes sures an empty string for word1 raises an error
        self.assertRaises(
            ValueError, edit_distance.edit_distance, "", "exponetial")
        # makes sures an empty string for word2 raises an error
        self.assertRaises(
            ValueError, edit_distance.edit_distance, "exponetial", "")
        # makes sures an empty string for both word1 and word2 raises an error
        self.assertRaises(ValueError, edit_distance.edit_distance, "", "")

    # Unit Tests for Edit Distance with Transpositions
    def test_edit_distance_transpositions(self):
        # Valid Cases
        self.assertEqual(edit_distance.edit_distance_transpositions(
            "snowy", "sonyw"), 2)  # tests valid words
        self.assertEqual(edit_distance.edit_distance_transpositions(
            "polynomial", "opylnomial"), 2)  # tests valid words

        # Boundary Cases
        self.assertEqual(edit_distance.edit_distance_transpositions(
            "a", "aaaaaaaaaaa"), 10)  # tests if there's only one character for word1
        self.assertEqual(edit_distance.edit_distance_transpositions(
            "a", "a"), 0)  # tests if both words are the same
        self.assertEqual(edit_distance.edit_distance_transpositions(
            "1", "123"), 2)  # tests strings with numbers
        self.assertEqual(edit_distance.edit_distance_transpositions(
            "exponential", "polynomial"), 6)  # tests strings when no transpositions are required

        # Erroneous Cases
        # makes sures an empty string for word1 raises an error
        self.assertRaises(
            ValueError, edit_distance.edit_distance_transpositions, "", "exponetial")
        # makes sures an empty string for word2 raises an error
        self.assertRaises(
            ValueError, edit_distance.edit_distance_transpositions, "exponetial", "")
        # makes sures an empty string for both word1 and word2 raises an error
        self.assertRaises(
            ValueError, edit_distance.edit_distance_transpositions, "", "")


if __name__ == '__main__':
    unittest.main()
