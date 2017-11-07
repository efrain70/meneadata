# -*- coding: utf-8 -*-
import logging

from six import Iterator

import requests
from bs4 import BeautifulSoup

from .page import Page

logger = logging.getLogger('Meneadata')


class MeneaData(Iterator):

    main_url = 'https://www.meneame.net/'
    go_page = '?page={}'

    def __init__(self, start_page=1, last_page=-1):
        self.current = start_page
        self.last_page = last_page

    def create_page(self, url):
        try:
            response = requests.get(url)
        except Exception as e:
            # Todo
            raise e
        else:
            bs_tag = BeautifulSoup(response.text, "html.parser")
            return Page(bs_tag)

    def __iter__(self):
        return self

    def __next__(self):
        if not self.last_page == -1 and self.last_page < self.current:
            raise StopIteration

        url = '{}{}'.format(self.main_url, self.go_page)

        try:
            logger.debug('Reading page: {}'.format(self.current))
            page = self.create_page(url.format(self.current))
            logger.debug('Finished page: {}'.format(self.current))

        except Exception as e:
            # Todo
            raise StopIteration
        else:
            self.current += 1
            return page

    next = __next__  # Python 2
