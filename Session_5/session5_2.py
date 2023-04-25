######## test4.py:  read file4.txt ########

""" test4.py:  open and read a file """

fh = open('file4.txt')   # add relative filepath here to open file4.txt

print(fh.read())         # this is file4.txt



######## test2b.py:  read file3b.txt ########

""" test2b.py:  open and read a file """

fh = open('dir3b/file3b.txt')            # add relative filepath here to open file3b.txt

print(fh.read())         # this is file3b.txt



######## test1.py:  read file3a.txt ########

""" test1.py:  open and read a file """

fh = open('dir2a/dir3a/file3a.txt')   # add relative filepath here to open file3a.txt

print(fh.read())         # this is file3a.txt



######## test2a.py:  read file1.txt ########

""" test2a.py:  open and read a file """

fh = open('../file1.txt')  # add relative filepath here to open file1.txt

print(fh.read())         # this is file1.txt



######## test3a.py:  read file1.txt ########

""" test3a.py:  open and read a file """

fh = open('../../file1.txt')  # add relative filepath here to open file1.txt

print(fh.read())         # this is file1.txt