# -*- coding: utf-8 -*-
from collections.abc import Iterator

from .meneo import Meneo

class MainPage(Iterator):

    meneo_class = "news-summary"

    def __init__(self, bs_tag):
        self.bs_tag = bs_tag
        self.meneo_divs = self._get_list_meneos_html()

    def _get_list_meneos_html(self):
        return iter(self.bs_tag.find_all("div", class_=self.meneo_class))

    def __iter__(self):
        return self

    def create_meneo(self, bs_tag):
        return Meneo(bs_tag)

    def __next__(self):
        bs_tag = next(self.meneo_divs)
        return self.create_meneo(bs_tag)

