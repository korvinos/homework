from urllib.request import urlopen
from urllib.parse import urljoin

from lxml.html import fromstring


URL = 'http://www.proglive.ru/courses'
ITEM_PATH = '.our-courses_list .our-courses_item .right'


def parse_courses():
    f = urlopen(URL)
    list_html = f.read().decode('utf-8')
    list_doc = fromstring(list_html)

    for elem in list_doc.cssselect(ITEM_PATH):
        a = elem.cssselect('a')[0]
        href = a.get('href')
        print(href)


def main():
    parse_courses()


if __name__ == '__main__':
    main()