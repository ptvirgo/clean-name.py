#! /usr/bin/env python3

import argparse
import os.path
import shutil
import re


"""Write a program that renames files specified at runtime.  The new name
should be lower case and characters that require escaping in BASH should be
removed or replaced."""


def clean_name(fn):
    """
    Clean up a file name.

    Parameters:  a file name, possibly including the absolute path
    Returns:  the file name with an intact path, case corrected and cleaned-up
    filename.
    """

    path = unix_split_basename(fn)
    file_name = path[1]

    file_name = re.sub("&", "_and_", file_name)
    file_name = re.sub("[\s]+", "_", file_name)

    # strip remaining escape characters
    file_name = re.sub("[^\w\.\~-]", "", file_name)

    # dedup _ and .

    file_name = re.sub("_+", "_", file_name)
    file_name = re.sub(
        "[_\.]*([\.\~-])_*", lambda match: match.groups()[0], file_name)

    return os.path.join(path[0], file_name.lower())


def unix_split_basename(fn):
    """
    Split a filename the same way an old-school unix basename would. A dir is
    still a file, we just want to split the parents from the last child.

    Parameters: a file name, preferably including absolute path
    Returns: tuple of the unix-style directory and basename for the provided
    file.  Unix style meaning that unlike os.path.basename, "/foo/bar/"
    returns ("/foo", "bar").
    """

    names = fn.split("/")

    basename = names.pop()

    while (basename == ''):
        basename = names.pop()

    dirs = "/".join(names)

    return (dirs, basename)


def main():
    """
    Rename the files as specified on the command line.
    """

    parser = argparse.ArgumentParser(
        description="Rename files with unix style names.")
    parser.add_argument('file_names', help="List of files to be renamed", nargs='+')
    args = parser.parse_args()

    for fn in args.file_names:
        nn = clean_name(fn)
        shutil.move(fn, nn)


if __name__ == '__main__':
    main()
