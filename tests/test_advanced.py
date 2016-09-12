# -*- coding: utf-8 -*-

from .context import dxster

import unittest

"""
ALGDx truth table

+--------+---------------------+---------------+-------------+-------------+----------------------+
| CDR_SB |    NPDX - NORMAL    | NPDX - PREMCI | NPDX - EMCI | NPDX - LMCI |   NPDX - DEMENTIA    |
+--------+---------------------+---------------+-------------+-------------+----------------------+
|        |                     |               |             |             |                      |
| 0      | Normal              | PreMCI - NP   | eMCI - NP   | LMCI - NP   | Consensus Conference |
|        |                     |               |             |             |                      |
| 2      | Normal              | PreMCI - NP   | eMCI - NP   | LMCI - NP   | Consensus Conference |
|        |                     |               |             |             |                      |
| 2.5    | PreMCI - CDR        | PreMCI        | eMCI        | LMCI        | LMCI                 |
|        |                     |               |             |             |                      |
| 4      | PreMCI - CDR        | PreMCI        | eMCI        | LMCI        | LMCI                 |
|        |                     |               |             |             |                      |
| >4.5   | Consesus Conference | Dementia      | Dementia    | Dementia    | Dementia             |
+--------+---------------------+---------------+-------------+-------------+----------------------+

"""

class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""


    """
      _   _ _____  _____                  _   _                            _
     | \ | |  __ \|  __ \        ______  | \ | |                          | |
     |  \| | |__) | |  | |_  __ |______| |  \| | ___  _ __ _ __ ___   __ _| |
     | . ` |  ___/| |  | \ \/ /  ______  | . ` |/ _ \| '__| '_ ` _ \ / _` | |
     | |\  | |    | |__| |>  <  |______| | |\  | (_) | |  | | | | | | (_| | |
     |_| \_|_|    |_____//_/\_\          |_| \_|\___/|_|  |_| |_| |_|\__,_|_|

    """


    # If ClinicalDx (CDR-sb) = 0-2.0 & NpDx = Normal  then AlgDx = ‘Normal’
    def test_calc_dxster_cdr_lowrange_npdx_normal(self):
        self.assertEqual(dxster.calc_dxster(0,'normal'), 'Normal')
        self.assertEqual(dxster.calc_dxster(.5,'normal'), 'Normal')
        self.assertEqual(dxster.calc_dxster(1,'normal'), 'Normal')
        self.assertEqual(dxster.calc_dxster(1.5,'normal'), 'Normal')
        self.assertEqual(dxster.calc_dxster(2.0,'normal'), 'Normal')

    # If ClinicalDx (CDR-sb) = 2.5-4.0 & NpDx = Normal then AlgDx = ‘PreMCI-CDR’
    def test_calc_dxster_cdr_midrange_npdx_normal(self):
       self.assertEqual(dxster.calc_dxster(2.5,'normal'), 'PreMCI-CDR')
       self.assertEqual(dxster.calc_dxster(3.0,'normal'), 'PreMCI-CDR')
       self.assertEqual(dxster.calc_dxster(3.5,'normal'), 'PreMCI-CDR')
       self.assertEqual(dxster.calc_dxster(4.0,'normal'), 'PreMCI-CDR')

    # If ClinicalDx (CDR-sb) >= 4.5 & NpDx = Normal then AlgDx = ‘Consensus Conference’"
    def test_calc_dxster_cdr_highrange_npdx_normal(self):
       self.assertEqual(dxster.calc_dxster(4.5,'normal'), 'Consensus Conference')
       self.assertEqual(dxster.calc_dxster(5.5,'normal'), 'Consensus Conference')


    """

      _   _ _____  _____                  _____  _____  ______ __  __  _____ _____
     | \ | |  __ \|  __ \        ______  |  __ \|  __ \|  ____|  \/  |/ ____|_   _|
     |  \| | |__) | |  | |_  __ |______| | |__) | |__) | |__  | \  / | |      | |
     | . ` |  ___/| |  | \ \/ /  ______  |  ___/|  _  /|  __| | |\/| | |      | |
     | |\  | |    | |__| |>  <  |______| | |    | | \ \| |____| |  | | |____ _| |_
     |_| \_|_|    |_____//_/\_\          |_|    |_|  \_\______|_|  |_|\_____|_____|


    """

    # If ClinicalDx (CDR-sb) = 0-2.0 & NpDx = premci  then AlgDx = PreMCI - NP
    def test_calc_dxster_cdr_lowrange_npdx_premci(self):
        self.assertEqual(dxster.calc_dxster(0,'premci'), 'PreMCI - NP')
        self.assertEqual(dxster.calc_dxster(.5,'premci'), 'PreMCI - NP')
        self.assertEqual(dxster.calc_dxster(1,'premci'), 'PreMCI - NP')
        self.assertEqual(dxster.calc_dxster(1.5,'premci'), 'PreMCI - NP')
        self.assertEqual(dxster.calc_dxster(2.0,'premci'), 'PreMCI - NP')

    # If ClinicalDx (CDR-sb) = 2.5-4.0 & NpDx = premci then AlgDx = ‘PreMCI’
    def test_calc_dxster_cdr_midrange_npdx_premci(self):
       self.assertEqual(dxster.calc_dxster(2.5,'premci'), 'PreMCI')
       self.assertEqual(dxster.calc_dxster(3.0,'premci'), 'PreMCI')
       self.assertEqual(dxster.calc_dxster(3.5,'premci'), 'PreMCI')
       self.assertEqual(dxster.calc_dxster(4.0,'premci'), 'PreMCI')

    # If ClinicalDx (CDR-sb) >= 4.5 & NpDx = premci then AlgDx = ‘Dementia’"
    def test_calc_dxster_cdr_highrange_npdx_premci(self):
       self.assertEqual(dxster.calc_dxster(4.5,'premci'), 'Dementia')
       self.assertEqual(dxster.calc_dxster(5.5,'premci'), 'Dementia')

    """

      _   _ _____  _____                  ______ __  __  _____ _____
     | \ | |  __ \|  __ \        ______  |  ____|  \/  |/ ____|_   _|
     |  \| | |__) | |  | |_  __ |______| | |__  | \  / | |      | |
     | . ` |  ___/| |  | \ \/ /  ______  |  __| | |\/| | |      | |
     | |\  | |    | |__| |>  <  |______| | |____| |  | | |____ _| |_
     |_| \_|_|    |_____//_/\_\          |______|_|  |_|\_____|_____|

    """
    # If ClinicalDx (CDR-sb) = 0-2.0 & NpDx = emci  then AlgDx = eMCI - NP
    def test_calc_dxster_cdr_lowrange_npdx_emci(self):
        self.assertEqual(dxster.calc_dxster(0,'emci'), 'eMCI - NP')
        self.assertEqual(dxster.calc_dxster(.5,'emci'), 'eMCI - NP')
        self.assertEqual(dxster.calc_dxster(1,'emci'), 'eMCI - NP')
        self.assertEqual(dxster.calc_dxster(1.5,'emci'), 'eMCI - NP')
        self.assertEqual(dxster.calc_dxster(2.0,'emci'), 'eMCI - NP')

    # If ClinicalDx (CDR-sb) = 2.5-4.0 & NpDx = premci then AlgDx = ‘PreMCI’
    def test_calc_dxster_cdr_midrange_npdx_emci(self):
       self.assertEqual(dxster.calc_dxster(2.5,'emci'), 'eMCI')
       self.assertEqual(dxster.calc_dxster(3.0,'emci'), 'eMCI')
       self.assertEqual(dxster.calc_dxster(3.5,'emci'), 'eMCI')
       self.assertEqual(dxster.calc_dxster(4.0,'emci'), 'eMCI')

    # If ClinicalDx (CDR-sb) >= 4.5 & NpDx = emci then AlgDx = ‘Dementia’"
    def test_calc_dxster_cdr_highrange_npdx_emci(self):
       self.assertEqual(dxster.calc_dxster(4.5,'emci'), 'Dementia')
       self.assertEqual(dxster.calc_dxster(5.5,'emci'), 'Dementia')





    """

      _   _ _____  _____                  _      __  __  _____ _____
     | \ | |  __ \|  __ \        ______  | |    |  \/  |/ ____|_   _|
     |  \| | |__) | |  | |_  __ |______| | |    | \  / | |      | |
     | . ` |  ___/| |  | \ \/ /  ______  | |    | |\/| | |      | |
     | |\  | |    | |__| |>  <  |______| | |____| |  | | |____ _| |_
     |_| \_|_|    |_____//_/\_\          |______|_|  |_|\_____|_____|



    """

    # If ClinicalDx (CDR-sb) = 0-2.0 & NpDx = lmci  then AlgDx = LMCI - NP
    def test_calc_dxster_cdr_lowrange_npdx_lmci(self):
        self.assertEqual(dxster.calc_dxster(0,'lmci'), 'LMCI - NP')
        self.assertEqual(dxster.calc_dxster(.5,'lmci'), 'LMCI - NP')
        self.assertEqual(dxster.calc_dxster(1,'lmci'), 'LMCI - NP')
        self.assertEqual(dxster.calc_dxster(1.5,'lmci'), 'LMCI - NP')
        self.assertEqual(dxster.calc_dxster(2.0,'lmci'), 'LMCI - NP')

    # If ClinicalDx (CDR-sb) = 2.5-4.0 & NpDx = premci then AlgDx = ‘PreMCI’
    def test_calc_dxster_cdr_midrange_npdx_lmci(self):
       self.assertEqual(dxster.calc_dxster(2.5,'lmci'), 'LMCI')
       self.assertEqual(dxster.calc_dxster(3.0,'lmci'), 'LMCI')
       self.assertEqual(dxster.calc_dxster(3.5,'lmci'), 'LMCI')
       self.assertEqual(dxster.calc_dxster(4.0,'lmci'), 'LMCI')

    # If ClinicalDx (CDR-sb) >= 4.5 & NpDx = emci then AlgDx = ‘Dementia’"
    def test_calc_dxster_cdr_highrange_npdx_lmci(self):
       self.assertEqual(dxster.calc_dxster(4.5,'lmci'), 'Dementia')
       self.assertEqual(dxster.calc_dxster(5.5,'lmci'), 'Dementia')

    """

      _   _ _____  _____                  _____  ______ __  __ ______ _   _ _______ _____
     | \ | |  __ \|  __ \        ______  |  __ \|  ____|  \/  |  ____| \ | |__   __|_   _|   /\
     |  \| | |__) | |  | |_  __ |______| | |  | | |__  | \  / | |__  |  \| |  | |    | |    /  \
     | . ` |  ___/| |  | \ \/ /  ______  | |  | |  __| | |\/| |  __| | . ` |  | |    | |   / /\ \
     | |\  | |    | |__| |>  <  |______| | |__| | |____| |  | | |____| |\  |  | |   _| |_ / ____ \
     |_| \_|_|    |_____//_/\_\          |_____/|______|_|  |_|______|_| \_|  |_|  |_____/_/    \_\


    """

    # If ClinicalDx (CDR-sb) = 0-2.0 & NpDx = Dementia  then AlgDx = LMCI - NP
    def test_calc_dxster_cdr_lowrange_npdx_dementia(self):
        self.assertEqual(dxster.calc_dxster(0,'dementia'), 'Consensus Conference')
        self.assertEqual(dxster.calc_dxster(.5,'dementia'), 'Consensus Conference')
        self.assertEqual(dxster.calc_dxster(1,'dementia'), 'Consensus Conference')
        self.assertEqual(dxster.calc_dxster(1.5,'dementia'), 'Consensus Conference')
        self.assertEqual(dxster.calc_dxster(2.0,'dementia'), 'Consensus Conference')

    # If ClinicalDx (CDR-sb) = 2.5-4.0 & NpDx = premci then AlgDx = ‘PreMCI’
    def test_calc_dxster_cdr_midrange_npdx_lmci(self):
       self.assertEqual(dxster.calc_dxster(2.5,'dementia'), 'LMCI')
       self.assertEqual(dxster.calc_dxster(3.0,'dementia'), 'LMCI')
       self.assertEqual(dxster.calc_dxster(3.5,'dementia'), 'LMCI')
       self.assertEqual(dxster.calc_dxster(4.0,'dementia'), 'LMCI')

    # If ClinicalDx (CDR-sb) >= 4.5 & NpDx = emci then AlgDx = ‘Dementia’"
    def test_calc_dxster_cdr_highrange_npdx_lmci(self):
       self.assertEqual(dxster.calc_dxster(4.5,'dementia'), 'Dementia')
       self.assertEqual(dxster.calc_dxster(5.5,'dementia'), 'Dementia')


if __name__ == '__main__':
    unittest.main()
