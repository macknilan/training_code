import unittest

from play_file_03 import main


class TestMain(unittest.TestCase):
    def test_main(self):
        # TEST STRING WITH VOWELS
        input_str = "hello world"
        result = main(input_str)
        self.assertEqual(result, 3)

        # STRING WITHOUT VOWELS
        input_str = "hll wrld"
        result = main(input_str)
        self.assertEqual(result, 0)

        # EMPTY STRING
        input_str = ""
        result = main(input_str)
        self.assertEqual(result, 0)


if __name__ == "__main__":
    unittest.main()
