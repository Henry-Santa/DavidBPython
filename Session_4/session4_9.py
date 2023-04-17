file_name = input("please enter a filename:  ") # str, 'sawyer.txt'

processing_file = open(file_name)               # 'File' object

data = processing_file.read()                   # str, the sawyer.txt text contents

word_count = len(data.split())                  # int, 270
line_count = len(data.split("\n"))              # int, 20
char_count = len(data.rstrip())                 # int, 1438

print(f"{line_count:>10} {word_count:>5} {char_count:>7} {file_name}".rjust(8))