import unittest
from clean_name import *

'''
Data Definitions:
'''

# Filename is string

FN1 = "/tmp/file.txt"
FN2 = "~/Downloads"

def function_for_filename(fn):
  # ... 
  return fn

class TestCleanName(unittest.TestCase):

  def test_clean_name(self):
    self.assertEqual(clean_name( "/HOME/USER/DOCUMENTS" ),
      "/HOME/USER/documents")
    self.assertEqual(clean_name( "/home/user/documents/noTes-2.TXT"),
      "/home/user/documents/notes-2.txt")
    self.assertEqual(clean_name(
      "/home/user/documents/N#o%p!`e(&)_thA$nks...TXT~"),
      "/home/user/documents/nope_and_thanks.txt~")
    self.assertEqual(clean_name( "/home/user/documents/so...much...win"),
      "/home/user/documents/so.much.win")

  def test_unix_split_basename(self):
    self.assertEqual(unix_split_basename("/foo/bar/"), ("/foo", "bar"))
    self.assertEqual(unix_split_basename("/foo/bar/baz"), ("/foo/bar", "baz"))
    self.assertEqual(unix_split_basename("foo"), ("", "foo"))

if __name__ == '__main__':
  unittest.main()
