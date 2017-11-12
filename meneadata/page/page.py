# -*- coding: utf-8 -*-
"""meneadata.page - Page módulo."""

from six import Iterator

from .meneo import Meneo


class Page(Iterator):
    """La clase Page representa una página de menéame.

    En ésta se muestran los meneos listados. Iterando a través de ella se
    obtienen éstos modelados con la clase Meneo.
    """

    meneo_class = "news-summary"

    def __init__(self, bs_tag):
        """Iniciliza la clase de la página.

        Inicializa la clase con un objeto bs4 Tab donde se contienen los meneos
        en sub elementos con la clase 'news-summary'.

        Args:
            bs_tag: elemento bs4 Tag que contiene los meneos.

        """
        self.bs_tag = bs_tag
        self.meneo_divs = self.bs_tag.find_all("div", class_=self.meneo_class)
        self._meneo_divs_iteartor = iter(self.meneo_divs)

    def __iter__(self):
        """Creador de iterator.

        Returns:
            El mismo objecto haciéndolo iterable.

        """
        return self

    def __next__(self):
        """
        Deuelve el siguiente meneo en la página.

        Returns:
            Siguiente meneo.

        """
        bs_tag = next(self._meneo_divs_iteartor)
        return Meneo(bs_tag)

    def __len__(self):
        """
        Devuelve el número de meneos en la página.

        Returns:
            El número de meneos en la página.

        """
        return len(self.meneo_divs)

    next = __next__  # Python 2
