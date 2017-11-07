# -*- coding: utf-8 -*-
from meneadata.page import Meneo


class TestPage(object):

    def test_iterator(self, valid_page):
        for index, meneo in enumerate(valid_page):
            assert isinstance(meneo, Meneo)
            assert meneo.title == 'Ruby off the Rails_' + str(index)
            assert meneo.votes == str(index)
            assert meneo.author == 'paco_' + str(index)

    def test_empty_page(self, empty_page):
        meneos = [meneo for meneo in empty_page]
        assert len(meneos) == 0

    def test_len(self, valid_page):
        assert len(valid_page) == 10

