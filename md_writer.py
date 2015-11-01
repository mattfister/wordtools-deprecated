__author__ = 'supergork'

import time
import os.path


out_file = open(os.path.join('output', str(int(time.time()))) + '.md', 'w')

def print_title(s):
    print('%'+s+'\n')
    out_file.write('%'+s+'\n')

def print_chapter_heading(s):
    print('#'+s+'\n')
    out_file.write('#'+s+'\n')

def print_chapter_sentence(s):
    print(s + ' ')
    out_file.write(s+' ')

def end_chapter():
    out_file.write(s)

