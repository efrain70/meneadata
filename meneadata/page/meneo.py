# -*- coding: utf-8 -*-
"""meneadata.meneo - Meneo módulo."""
import re

from six import Iterator


class Meneo(Iterator):
    """Esta clase modela un meneo en la página.

    Facilita la lectura de los atributos más importantes de éste. También con
    iteración se pueden obtener éstos.

    """
    headers = ['votes', 'title', 'author', 'n_comments', 'karma', 'timestamp']
    vote_class = 'votes'
    author_class = 'news-submitted'
    timestamp_class = 'ts'
    karma_class = 'karma-value'
    comments_class = 'comments'

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

    @property
    def n_comments(self):
        """Devuelve el número de comentarios.

        Returns:
            Número de comentarios del meneo.

        """
        comments = self.bs_tag.find('a', class_=self.comments_class)
        text_comments = comments.text.strip()
        numbers = re.findall(r'\d+', text_comments)

        if numbers:
            return numbers[0]
        else:
            return '0'

    @property
    def karma(self):
        """Devuelve el karma del meneo.

        Returns:
            Valor de karma del meneo.

        """
        karma = self.bs_tag.find('span', class_=self.karma_class)
        return karma.text.strip()

    @property
    def timestamp(self):
        """Devuelve el timestamp del meneo.

        Returns:
            Valor del timestaop del meneo.

        """
        time_stamp = self.bs_tag.find('span', class_=self.timestamp_class)
        return time_stamp.get('data-ts')

    def __iter__(self):
        """Principales atributos del meneo: votes, title y author.

        Returns:
            Iterando devuelve el atributo correspondiente.

        """
        yield self.votes
        yield self.title
        yield self.author
        yield self.n_comments
        yield self.karma
        yield self.timestamp

    def __next__(self):
        """Devuelve el siguiente atributo.

        Returns:
            El siguiente atributo.

        """
        return self.__iter__()

    next = __next__  # Python 2
