# -*- coding: utf-8 -*-
import requests

from collections.abc import Iterator

from .page.main import MainPage


class MeneaData(Iterator):

    main_url = 'https://www.meneame.net/'
    go_page = '?page={}'

    def __init__(self, max_pages=None):
        self.current = 0
        self.max_pages = max_pages

    def create_page(self, url):
        try:
            response = requests.get(url)
        except Exception as e:
            # todo
            raise e
        else:
            return MainPage(response.text)

    def __iter__(self):
        return self

    def __next__(self):
        if self.max_pages is not None and self.max_pages > self.current:
            raise StopIteration

        if self.current == 0:
            url = self.main_url
        else:
            url = '{}{}'.format(self.main_url, self.go_page)

        self.current += 1

        try:
            return self.create_page(url.format(self.current))
        except Exception as e:
            raise StopIteration


def main():
    print('meneadata output')
    return 0
