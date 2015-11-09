__author__ = 'supergork'

import time
import os.path
import subprocess
import pypandoc

name = str(int(time.time()))
md_name = name + '.md'
html_name = name + '.html'
md_file_path = os.path.join('output', md_name)
html_file_path = os.path.join('output', html_name)
out_file = open(md_file_path, 'w')


def print_title(s):
    print('%'+s+'\n')
    out_file.write('%'+s+'\n')

def print_chapter_heading(s):
    print('#'+s+'\n')
    out_file.write('#'+s+'\n')

def print_chapter_sentence(s):
    print(s + ' ')
    out_file.write(s+' ')

def end_paragraph():
    out_file.write('\n\n')

def end_chapter():
    out_file.write('\n\n')

def end_novel():
    out_file.close()
    pandoc_cmd = ['pandoc ', md_file_path, '-f', 'markdown','-t', 'html', '-s', '-o', html_file_path]
    pypandoc.convert(md_file_path, 'html', outputfile=html_file_path, extra_args=['-s'])

