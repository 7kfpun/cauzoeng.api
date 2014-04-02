#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tests  # nolint


def test_test():
    assert 1 == 1

# lint_ignore=W0401

import os
import sys


sys.path.append(os.path.join(os.path.dirname(__file__), 'libs'))
sys.path.append(os.path.dirname(__file__))
