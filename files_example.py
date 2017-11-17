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

# check if directory exists
if not os.path.isdir(dirname):
    # if it does not, create it
    os.mkdir(dirname)


idx = len(os.listdir(dirname))
idx_str = str(idx)

file_text = 'This is an example file.\n'

filename = os.path.join(dirname, idx_str + '.txt')

with open(filename, 'w+') as f:
    f.write(file_text)
