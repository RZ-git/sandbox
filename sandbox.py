import os
import sys
from pprint import pprint
from bs4 import BeautifulSoup
from urllib import request


# sys.path.append(os.path.join(os.path.dirname(__file__), 'site-packages'))


class ModuleTest:

    def __init__(self):
        super().__init__()

    @staticmethod
    def run_beautiful_soup(url='https://www.octoparse.jp/blog/top-30-free-web-scraping-software/'):
        # スクレイピング
        response = request.urlopen(url)
        soup = BeautifulSoup(response)
        text_by_line = soup.text.split('\n')
        selected_tool_names = [name for name in text_by_line if '.' in name]
        pprint(selected_tool_names)

        response.close()


print('████████████████ S T A R T ████████████████')
mt = ModuleTest()

mt.run_beautiful_soup()
print('██████████████████ E N D ██████████████████')
