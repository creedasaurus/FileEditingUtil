# Purpose: Add override to the files found in list.txt
#           format for list .txt is [file Name], [Line Number]

import sys
import re
import argparse
import os


def fixFiles(file_name):
    find_line = re.compile("virtual [\w]+ [\w]+\(\);")
    data = []
    with open(file_name, 'r+') as in_file:
        data = in_file.readlines()

    for indx, line in enumerate(data):
        if find_line.search(line):
            data[indx] = line.replace(';', ' override;')

    with open(file_name, 'w') as out_file:
        out_file.writelines(data)


def validate_file(pars, arg):
    if not os.path.exists(arg):
        pars.error(f'File {arg} does not exist')
    else:
        return arg


def validate_searchterm(pars, arg):
    try:
        reg = re.compile(arg.encode().decode('unicode_escape'))
    except Exception:
        pars.error(f'{arg} is not a good regex -- try again')
    else:
        return reg


if __name__ == "__main__":
    fixFiles("testing.txt")
    # parser = argparse.ArgumentParser(description="add_override v0.2")
    # parser.add_argument("-i", "--infile", metavar="FILE-DIR",
    #                     help="file or directory of target files to change",
    #                     type=lambda x: validate_file(parser, x))
    # parser.add_argument("-r", "--regex", metavar="REGEX",
    #                     help="regex to replace",
    #                     type=lambda x: validate_searchterm(parser, x))
    # args = parser.parse_args()
    # print(args)
    # newtest = "That was reall cool, buzz!"
    # print(args.regex.search(newtest))
