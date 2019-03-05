import unittest
from clean_name import clean_name, unix_split_basename


class TestCleanName(unittest.TestCase):

    def test_clean_name_lowercases(self):
        """clean_name() should lowercase file names"""
        self.assertEqual(
            clean_name("/HOME/USER/DOCUMENTS"), "/HOME/USER/documents")

        self.assertEqual(
            clean_name("/home/user/documents/noTes-2.TXT"),
            "/home/user/documents/notes-2.txt")

    def test_clean_name_character_cleanup(self):
        """clean_name() should drop weird characters"""

        self.assertEqual(clean_name(
            "/home/user/documents/N#o%p!`e(&)_thA$nks...TXT~"),
            "/home/user/documents/nope_and_thanks.txt~")

        self.assertEqual(
            clean_name("/home/user/documents/so...much...win"),
            "/home/user/documents/so.much.win")

        self.assertEqual(
            clean_name("/home/user/something_.txt"),
            "/home/user/something.txt")

        self.assertEqual(
            clean_name("/home/user/something._txt"),
            "/home/user/something.txt")

    def test_unix_split_basename(self):
        self.assertEqual(unix_split_basename("/foo/bar/"), ("/foo", "bar"))
        self.assertEqual(unix_split_basename("/foo/bar/baz"), ("/foo/bar", "baz"))
        self.assertEqual(unix_split_basename("foo"), ("", "foo"))


if __name__ == '__main__':
    unittest.main()
