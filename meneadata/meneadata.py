# -*- coding: utf-8 -*-
from __future__ import print_function

import argparse
import csv
import logging
import sys

from .page.menedata import MeneaData
from .page.meneo import Meneo
from .version import version as __version__


logger = logging.getLogger('Meneadata')


def main():
    parser = argparse.ArgumentParser(prog='meneadata',
                                     description='MeneaData command')
    parser.add_argument('-f', nargs='?',
                        help='Path to file output', required=True)
    parser.add_argument('-s', nargs='?', help='first page', default=1)
    parser.add_argument('-l', nargs='?', help='last page', default=-1)
    parser.add_argument('-v', '--verbosity', action="store_true",
                        help='increase output verbosity')
    parser.add_argument('-log', nargs='?', help='log output file',
                        default='')

    args = parser.parse_args()

    filename = str(args.f)
    start_page = int(args.s)
    last_page = int(args.l)
    log_file = str(args.log)

    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    if args.verbosity:
        level = logging.DEBUG
    else:
        level = logging.INFO

    if log_file:
        ch = logging.FileHandler(filename=log_file)
    else:
        ch = logging.StreamHandler(sys.stdout)

    ch.setFormatter(formatter)
    logger.setLevel(level)
    logger.addHandler(ch)

    logger.info("Executing MeneaData version %s." % __version__)

    meneadata = MeneaData(start_page=start_page, last_page=last_page)

    with open(filename, 'w') as file_csv:
        writer = csv.writer(file_csv, delimiter=';',
                            quoting=csv.QUOTE_NONNUMERIC, lineterminator='\n')

        writer.writerow([header for header in Meneo.headers])

        logger.info('Starting in page: {}'.format(str(meneadata.current)))

        for page in meneadata:
            for meneo in page:
                writer.writerow([value for value in meneo])

        logger.info('Last page found: {}'.format(str(meneadata.current - 1)))

    return 0
