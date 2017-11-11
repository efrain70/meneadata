# -*- coding: utf-8 -*-
"""meneadata.meneadata - MeneaData módulo."""

import logging

import requests
from six import Iterator
from bs4 import BeautifulSoup

from .page import Page

logger = logging.getLogger('Meneadata')


class MeneaData(Iterator):
    """Clase principal para iterar por el conjunto de datos.

    Esta clase facilita la iteración por las páginas de menéame y la creación
    de objectos de la clase Page.
    """

    main_url = 'https://www.meneame.net/'
    go_page = '?page={}'

    def __init__(self, start_page=1, last_page=-1):
        """
        Inicializa la clase con una página por donde comenzar y un final.

        Args:
            start_page: página por dónde comenzar.
            last_page: página donde acabar, si -1 la última algún meneo.

        """
        self.current = start_page
        self.last_page = last_page

    def create_page(self, url):
        """Crea un objecto de la clase Page.

        Con el contenido de la respuesta obtenida a llamar la url dada se crea
        un objecto de la clase Page.

        Args:
            url: url para ser leida.

        Returns:
            objeto de la clase Page

        """
        response = requests.get(url)
        bs_tag = BeautifulSoup(response.text, "html.parser")
        return Page(bs_tag)

    def __iter__(self):
        """Creador de iterator.

        Returns:
            El mismo objecto haciéndolo iterable.

        """
        return self

    def __next__(self):
        """Devuelve la siguiente página a partir de la página de cominezo.

        Si la siguiente página no tiene ningún meneo significa que ya no hay
        más páginas para devolver.

        Returns:
            La siguiente página.

        Raises:
            StopIteration: no hay más páginas que devolver.

        """
        if not self.last_page == -1 and self.last_page < self.current:
            raise StopIteration

        url = '{}{}'.format(self.main_url, self.go_page)

        logger.debug('Reading page: {}'.format(self.current))
        page = self.create_page(url.format(self.current))
        logger.debug('Finished page: {}'.format(self.current))

        if len(page) == 0:
            logger.debug('Page: {} is empty.'.format(self.current))

            # Empty page is the last one
            raise StopIteration

        self.current += 1
        return page

    next = __next__  # Python 2
