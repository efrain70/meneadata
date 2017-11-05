# -*- coding: utf-8 -*-
import sys

from .page.main import MainPage
from .version import version as __version__


def main():
    print("Executing bootstrap version %s." % __version__)
    print("List of argument strings: %s" % sys.argv[1:])
    print("MainPage and MainPage():\n%s\n%s" % (MainPage, MainPage()))
