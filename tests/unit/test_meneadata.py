"""Library unit tests."""

import mock

from meneadata.page.menedata import MeneaData


@mock.patch('requests.get')
class TestMeneaData(object):

    def test_all(self, get, list_of_pages):
        get.side_effect = list_of_pages
        data = MeneaData()
        n_pages = 0
        n_meneos = 0
        for page_i, page in enumerate(data):
            n_pages += 1
            for meneo_i, meneo in enumerate(page):
                n_meneos += 1
                assert meneo.author == 'author_{}_{}'.format(page_i, meneo_i)
                assert meneo.title == 'title_{}_{}'.format(page_i, meneo_i)
                assert meneo.votes == str(meneo_i)

        assert n_pages == 10
        assert n_meneos == 10 * 10
        base_url = 'https://www.meneame.net/?page={}'

        calls = [mock.call(base_url.format(i)) for i in range(1, 12)]
        get.assert_has_calls(calls, True)

    def test_no_pages(self, get, empty_page_response):
        get.side_effect = [empty_page_response, ]

        data = MeneaData()
        pages = [page for page in data]

        get.assert_called_once_with('https://www.meneame.net/?page=1')

        meneos = [meneo for page in pages for meneo in page]

        assert len(pages) == 0
        assert len(meneos) == 0

    def test_not_in_range(self, get):
        data = MeneaData(start_page=12, last_page=11)

        pages = [page for page in data]

        get.assert_not_called()

        meneos = [meneo for page in pages for meneo in page]

        assert len(pages) == 0
        assert len(meneos) == 0

    def test_only_in_range(self, get, list_of_pages):
        data = MeneaData(start_page=3, last_page=8)
        get.side_effect = list_of_pages

        pages = [page for page in data]

        meneos = [meneo for page in pages for meneo in page]

        assert len(pages) == 6
        assert len(meneos) == 6 * 10

        base_url = 'https://www.meneame.net/?page={}'
        calls = [mock.call(base_url.format(i)) for i in range(3, 9)]
        get.assert_has_calls(calls, True)
