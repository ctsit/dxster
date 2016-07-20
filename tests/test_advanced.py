# -*- coding: utf-8 -*-

from .context import dxster

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        dxster.hmm()

    def test_calc_dxster_fail_test(self):
        self.assertTrue(dxster.calc_dxster('a','b'))

    # If ClinicalDx (CDR-sb) = 0-2.0 & NpDx = Normal  then AlgDx = ‘Normal’
    def test_calc_dxster_cdr_lowrange_npdx_normal(self):
        self.assertEqual(dxster.calc_dxster(0,'Normal'), 'Normal')

    # If ClinicalDx (CDR-sb) = 2.5-4.0 & NpDx = Normal then AlgDx = ‘PreMCI-CDR’
    def test_calc_dxster_cdr_midrange_npdx_normal(self):
        self.assertEqual(dxster.calc_dxster(2.5,'Normal'), 'Normal')

    # If ClinicalDx (CDR-sb) >= 4.5 & NpDx = Normal then AlgDx = ‘Consensus Conference’"
    def test_calc_dxster_cdr_highrange_npdx_normal(self):
        self.assertEqual(dxster.calc_dxster(5.5,'Normal'), 'Normal')



if __name__ == '__main__':
    unittest.main()
