'''
Run this like so:

    python example.py

It will create a directory 'files_dir' if it
doesn't exist then put a new random text file in there.
The file name before ".txt" will be one greater
for each new file added to the files directory.
'''
import os

dirname = 'files_dir'

# Check if directory exists.
if not os.path.isdir(dirname):
    # If it does not, create it.
    os.mkdir(dirname)

# See how many files are in files_dir.
idx = len(os.listdir(dirname))
# Convert that number to a string.
idx_str = str(idx)
# Some fake text to go in our new file..
file_text = 'This is an example file.\n'
# Create a filename; note this depends on no other person/program.
# Putting a file with a name like <integer>.txt.
filename = os.path.join(dirname, idx_str + '.txt')

# This is the most common way to handle writing to files in Python.
# This is also the most idiomatic Python-"Pythonic" for short.
with open(filename, 'w+') as f:
    f.write(file_text)
