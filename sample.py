import bs4 as bs
import urllib.request

sauce = urllib.request.urlopen('http://ksuweb.kennesaw.edu/~yshi5/7125/CS_7125_Homepage_spring2017.htm').read()

soup = bs.BeautifulSoup(sauce, 'lxml')

for paragraph in soup.find_all('p'):
    print(paragraph.text)
