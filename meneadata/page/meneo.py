# -*- coding: utf-8 -*-
from six import Iterator


class Meneo(Iterator):

    headers = ['votes', 'title', 'author']
    vote_class = 'votes'

    def __init__(self, bs_tag):
        self.bs_tag = bs_tag

    @property
    def title(self):
        return self.bs_tag.find('h2').text.strip()

    @property
    def votes(self):
        votes = self.bs_tag.find('div', class_=self.vote_class)
        return votes.find('a').text

    @property
    def author(self):
        author_image = self.bs_tag.find('div', class_='news-submitted')
        return author_image.find_all('a')[1].text

    def __iter__(self):
        yield self.votes
        yield self.title
        yield self.author

    def __next__(self):
        return self.__iter__()

    next = __next__  # Python 2
