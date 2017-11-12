# -*- coding: utf-8 -*-
from meneadata.page import Meneo


class TestMeneo(object):

    def test_author(self, valid_meneo):
        assert valid_meneo.author == 'paco'

    def test_title(self, valid_meneo):
        assert valid_meneo.title == 'Ruby off the Rails'

    def test_votes(self, valid_meneo):
        assert valid_meneo.votes == '24'

    def test_karma(self, valid_meneo):
        assert valid_meneo.karma == '165'

    def test_timestamp(self, valid_meneo):
        assert valid_meneo.timestamp == '1135515250'

    def test_n_comments(self, valid_meneo):
        assert valid_meneo.n_comments == '1123'

    def test_no_comments(self, no_comments_meneo):
        assert no_comments_meneo.n_comments == '0'

    def test_headers(self):
        assert Meneo.headers == ['votes', 'title', 'author', 'n_comments',
                                 'karma', 'timestamp']

    def test_iterator(self, valid_meneo):
        assert ['24',
                'Ruby off the Rails',
                'paco',
                '1123',
                '165',
                '1135515250',
                ] == [x for x in valid_meneo]

    def test_next(self, valid_meneo):
        iterator = next(valid_meneo)
        assert ['24',
                'Ruby off the Rails',
                'paco',
                '1123',
                '165',
                '1135515250',
                ] == [x for x in iterator]
