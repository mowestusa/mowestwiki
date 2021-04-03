import os
import re
import glob
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('--other', help='Specify Other Section Title', default='Other', type=str)
parser.add_argument('--home-page', help='Home Url', default='/', type=str)
parser.add_argument('--home-name', help='Home Name', default='Home', type=str)
parser.add_argument('--exclude', help='Exclude files from indexing', type=list, default=['README.md'])

args = parser.parse_args()

CATEGORY_KEY = 'Category'
OTHER_CATEGORY = args.other

categories = {}

print('* [{}]({})'.format(args.home_name, args.home_page))

for file in glob.glob('*.md'):
    if file[0] == '_' or file in args.exclude:
        continue
    with open(file, 'r') as f:
        content = f.read()
        begin = re.search(r'<\!--', content)
        end = re.search(r'-->', content)
        category_found = False
        category = None
        if begin is not None and end is not None:
            markup = content[begin.end():end.start()].strip()
            for line in markup.splitlines():
                fields = line.split(':')
                if len(fields) < 2:
                    continue
                if fields[0].strip().lower() == CATEGORY_KEY.lower():
                    category = fields[1].strip()        
                    category_found = True
        if not category_found:
            category = OTHER_CATEGORY
        begin = re.search(r'^# ', content)
        if begin is None:
            begin = re.search(r'\n#', content)
        if begin is None:
            continue
        title = content[begin.start()+1:content.find('\n', begin.start()+1)]
        title = title[1:].strip()
        if category not in categories:
            categories[category] = []
        categories[category].append({
            'title' : title,
            'file' : file
        })
                
other_table = None
for category in categories:
    if category == OTHER_CATEGORY:
        other_table = category
        continue
    print('* {}'.format(category))
    for item in categories[category]:
        print('\t* [{}](/{})'.format(item['title'], item['file']))

if other_table is not None:
    print('* {}'.format(OTHER_CATEGORY))
    for item in categories[category]:
        print('\t* [{}](/{})'.format(item['title'], item['file']))