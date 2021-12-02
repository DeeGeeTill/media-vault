# Converting Obsidian Markdown to Hugo-compatible markdown. 

import os
import sys
import subprocess
import time
import re

#Get list of all markdown files in current directory
def get_file_list():
    files = []
    for file in os.listdir():
        if file.endswith('.md'):
            files.append(file)
    return files

file_list = get_file_list()

#Add front matter to one file
def add_front_matter(file):
    #Remove file extension from file name
    file_name = file.split('.')[0]
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    with open(file, 'w', encoding='utf-8') as f:
        f.write('---\n')
        f.write('title: ' + file_name + '\n')
        f.write('date: "' + time.strftime("%Y-%m-%d") + '"\n')
        f.write('---\n')
        f.write(content)

#Remove front matter from all files while keeping line breaks

'''
def remove_front_matter(file):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    with open(file, 'w', encoding='utf-8') as f:
        print("entered front matter file open")
        #Find content between --- and --- and save to variable front_matter
        for match in re.finditer(r'---(.*?)---', content):
            front_matter = match.group(1)
            #Replace --- with nothing
            print("entered loop")
            content = content.replace(str(match.group()), '')
            print(front_matter)
        f.write(content)
        print("now writing content")
'''

#Convert all wikilinks to markdown links [Link](Link) instead of [[Link]]
def convert_wikilinks(file):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    with open(file, 'w', encoding='utf-8') as f:
        #Find content between [[ and ]] and save to variable link
        for match in re.finditer(r'\[\[(.*?)\]\]', content):
            link = match.group(1)
            link2 = link.replace(' ', '%20')
            print(link)
            #Replace [[ with [ and ]] with ]
            content = content.replace(str(match.group()), '[{}]({})'.format(link, link2))
            print("replaced a link")
            print(str(match.group()))
        f.write(content)


#Run add_front_matter on all files in file_list array
for file in file_list:
    add_front_matter(file)
    #Print progress to terminal
    print('Added to: ' + file)
    convert_wikilinks(file)
    print('Converted links in: ' + file)
