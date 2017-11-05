# -*- coding: utf-8 -*-
from collections.abc import Iterable


class Meneo(Iterable):

    headers = ['votes', 'title', ]
    vote_class = 'votes'

    def __init__(self, bs_tag):
        self.bs_tag = bs_tag

    @property
    def title(self):
        return self.bs_tag.find('h2').text

    @property
    def votes(self):
        votes = self.bs_tag.find('div', class_=self.vote_class)
        return votes.find('a').text

    def __iter__(self):
        yield self.votes
        yield self.title
