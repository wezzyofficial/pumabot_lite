#!/usr/bin/env /python3

import requests
from bs4 import BeautifulSoup


# example get_aneks()
# example get_aneks(count=10)
# example get_aneks(delimeter='')

def get_aneks(url='https://www.anekdot.ru/random/anekdot/',
              count=1,
              header={
                  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'},
              delimeter="#" * 20):
    result = requests.get(url, headers=header)
    with open('test.html', 'w') as output_file:
        output_file.write(str(result.text))
    html_file = open("test.html", "r")
    html_file_text = html_file.read()

    soup = BeautifulSoup(html_file_text, "lxml")
    aneks = soup.find_all('div', 'text')

    clear_aneks = []
    count = int(count)
    if count > len(aneks): count = len(aneks)
    for item in range(1, count + 1):
        anek = delimeter + '\n' + aneks[item].get_text() + '\n' + delimeter

        # anek = str(aneks[item]).replace('<div class="text">',"").replace("</div>","").replace("<br><br/>","\n").replace("<br/>","\n").replace("&quote;",'"').replace('\\n',' ')
        clear_aneks.append(anek)
    return clear_aneks