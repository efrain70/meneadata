# -*- coding: utf-8 -*-
import os


class TestMain(object):

    def test_command_return_value(self):
        assert os.system("meneadata") == 0

    def test_command_output(self):
        output = os.popen("meneadata").read()
        assert output == 'meneadata output\n'
