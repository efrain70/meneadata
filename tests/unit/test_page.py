# -*- coding: utf-8 -*-
from meneadata.page.meneo import Meneo


class TestPage(object):

    def test_iterator(self, valid_page):
        for index, meneo in enumerate(valid_page):
            assert isinstance(meneo, Meneo)
            assert meneo.title == 'Ruby off the Rails_' + str(index)
            assert meneo.votes == str(index)
            assert meneo.author == 'paco_' + str(index)
