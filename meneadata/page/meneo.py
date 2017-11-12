# -*- coding: utf-8 -*-
"""meneadata.meneo - Meneo módulo."""

from six import Iterator


class Meneo(Iterator):
    """Esta clase modela un meneo en la página.

    Facilita la lectura de los atributos más importantes de éste. También con
    iteración se pueden obtener éstos.

    """

    headers = ['votes', 'title', 'author']
    vote_class = 'votes'
    author_class = 'news-submitted'

    def __init__(self, bs_tag):
        """Inicializa la clase con un objecto bs4 Tag.

        Args:
            bs_tag: objeto bs4 Tag con el contenio del meneo.

        """
        self.bs_tag = bs_tag

    @property
    def title(self):
        """Devuelve el título del meneo.

        Returns:
            Título del meneo.

        """
        return self.bs_tag.find('h2').text.strip()

    @property
    def votes(self):
        """Devuelve el número de meneos que tiene el meneo.

        Returns:
            Número de meneos actuales.

        """
        votes = self.bs_tag.find('div', class_=self.vote_class)
        return votes.find('a').text

    @property
    def author(self):
        """Devuelve el autor del meneo.

        Returns:
            Autor del meneo.

        """
        author_image = self.bs_tag.find('div', class_=self.author_class)
        return author_image.find_all('a')[1].text

    def __iter__(self):
        """Principales atributos del meneo: votes, title y author.

        Returns:
            Iterando devuelve el atributo correspondiente.

        """
        yield self.votes
        yield self.title
        yield self.author

    def __next__(self):
        """Devuelve el siguiente atributo.

        Returns:
            El siguiente atributo.

        """
        return self.__iter__()

    next = __next__  # Python 2
