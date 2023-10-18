# -*- coding: utf-8 -*-

import os
import sys
from bs4 import BeautifulSoup

html_file = 'kb_20231014.html'

def main():
    if sys.argv and len(sys.argv) > 1:
        data_dir = sys.argv[1]
    else:
        return

    html_in_file = os.path.join(data_dir, html_file)
    with open(html_in_file, 'rb') as fp:
        soup = BeautifulSoup(fp, 'html.parser')
    
    for el in soup.find_all('table',{'class':'summarytable'}):
        el.insert_before('<div class="tableWrapper">')
        el.insert_after('</div>')
        print(el)

    for el in soup.find_all('table',{'class':'racetable'}):
        el.insert_before('<div class="tableWrapper">')
        el.insert_after('</div>')
        print(el)


    html_out_file = os.path.join(data_dir, f'out_{html_file}')
    with open(html_out_file, 'w', encoding='utf-8') as file:
        s = str(soup)
        s = s.replace('&lt;div class="tableWrapper"&gt;', '<div class="tableWrapper">')
        s = s.replace('&lt;/div&gt;', '</div>')
        s = s.replace('Ä—', 'ė')
        s = s.replace('ë', 'ė')
        s = s.replace('Ð', 'Š')
        s = s.replace('ð', 'š')
        s = s.replace('è', 'č')
        s = s.replace('ø', 'ų')
        s = s.replace('Å³', 'ų')
        s = s.replace('û', 'ū')
        s = s.replace('Ð', 'Š')
        s = s.replace('Å¾', 'ž')
        
        file.write(s)        
    pass


if __name__ == "__main__":
    main()