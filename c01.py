import unittest
import string


class WorkshopTest(unittest.TestCase):

    word = "string"
    lett = 1

    def test_letter_in_word(self):
        self.assertNotIn(str(self.lett), string.ascii_letters, "This is not letter.")
        self.assertIn(str(self.lett), self.word, "Not in word.")

    def test_instance(self):
        char_type = type(self.lett)
        self.assertIsInstance(self.lett, str, "This is: {}.".format(char_type))

    def test_not_one_char(self):
        lett_len = len(str(self.lett))
        self.assertLessEqual(1, lett_len, "More than one character. It have {} characters.".format(lett_len))

    def test_not_empty(self):
        lett_len = len(str(self.lett))
        self.assertEqual(lett_len, 0, "There is no letter.")


if __name__ == '__main__':
    unittest.main()
