import requests
from bs4 import BeautifulSoup
import re

class Scraper:
    def __init__(self):
        self.standard_headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
        }
        self.numberPattern = re.compile('[0-9]+')

class AndroidScraper(Scraper):
    def __init__(self):
        super(AndroidScraper, self).__init__()
        self.url = "https://vladsonkin.com/android-newsletter/"
        self.prefix = "Android Newsletter #"

    def get_newest(self):
        content = requests.get(self.url, headers=self.standard_headers).content
        soup = BeautifulSoup(content, "html.parser")

        versions = []
        for a in soup.find_all('a', string=re.compile(self.prefix)):
            linktext = a.contents[0]
            match = self.numberPattern.search(linktext)
            number = match.group()
            versions.append(int(number))
        else:
            return max(versions)

class KotlinScraper(Scraper):
    def __init__(self):
        super(KotlinScraper, self).__init__()
        self.url = "https://blog.jetbrains.com/kotlin/"
        self.classname = "post-thumbnail-wrap"

    def get_newest(self):
        content = requests.get(self.url, headers=self.standard_headers).content
        soup = BeautifulSoup(content, "html.parser")

        postpattern = re.compile('post-[0-9]+')
        newest_post = soup.find_all('article', {'id': postpattern})[0]
        return newest_post.get('id')