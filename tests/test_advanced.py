# -*- coding: utf-8 -*-

from .context import dxster

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        dxster.hmm()


if __name__ == '__main__':
    unittest.main()
