# -*- coding: utf-8 -*-
from meneadata.page.meneo import Meneo


class TestMeneo(object):

    def test_author(self, valid_meneo):
        assert valid_meneo.author == 'paco'

    def test_title(self, valid_meneo):
        assert valid_meneo.title == 'Ruby off the Rails'

    def test_votes(self, valid_meneo):
        assert valid_meneo.votes == '24'

    def test_headers(self):
        assert Meneo.headers == ['votes', 'title', 'author']

    def test_iterator(self, valid_meneo):
        assert ['24', 'Ruby off the Rails', 'paco'] == [x for x in valid_meneo]
