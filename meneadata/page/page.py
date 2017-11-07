# -*- coding: utf-8 -*-
from six import Iterator

from .meneo import Meneo


class Page(Iterator):

    meneo_class = "news-summary"

    def __init__(self, bs_tag):
        self.bs_tag = bs_tag
        self.meneo_divs = self.bs_tag.find_all("div", class_=self.meneo_class)
        self._meneo_divs_iteartor = iter(self.meneo_divs)

    def __iter__(self):
        return self

    def create_meneo(self, bs_tag):
        return Meneo(bs_tag)

    def __next__(self):
        bs_tag = next(self._meneo_divs_iteartor)
        return self.create_meneo(bs_tag)

    def __len__(self):
        return len(self.meneo_divs)

    next = __next__  # Python 2
