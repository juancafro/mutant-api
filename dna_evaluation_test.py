import unittest

import is_mutant


class DnaValidationTest(unittest.TestCase):

    def test_identify_horizontal_sequences(self):
        dna_with_two_horizontal_sequences = ["ATAAAA",
                                             "CTGTGC",
                                             "TTGTGT",
                                             "AGAAGG",
                                             "CCCCTA",
                                             "TCACTG"]
        dna_is_mutant = is_mutant.is_mutant_dna(dna_with_two_horizontal_sequences)
        self.assertEqual(dna_is_mutant, True)

    def test_identify_vertical_sequences(self):
        dna_with_two_vertical_sequences = ["ATAAAG",
                                           "CTGTCG",
                                           "ATAGAG",
                                           "ATATGG",
                                           "CACATA",
                                           "TCACTG"]
        dna_is_mutant = is_mutant.is_mutant_dna(dna_with_two_vertical_sequences)
        self.assertEqual(dna_is_mutant, True)

    def test_identify_inverse_diagonal_sequences(self):
        dna_with_two_inverse_diagonal_sequences = ["ACATAG",
                                                   "CTGAGA",
                                                   "ATAGAA",
                                                   "ATGTAG",
                                                   "CACATA",
                                                   "TCACTG"]
        dna_is_mutant = is_mutant.is_mutant_dna(dna_with_two_inverse_diagonal_sequences)
        self.assertEqual(dna_is_mutant, True)

    def test_identify_diagonal_sequences(self):
        dna_with_two_diagonal_sequences = ["ACATCG",
                                           "CAGAGA",
                                           "CTAGAA",
                                           "ACGAGG",
                                           "CACATA",
                                           "TCTCTG"]
        dna_is_mutant = is_mutant.is_mutant_dna(dna_with_two_diagonal_sequences)
        self.assertEqual(dna_is_mutant, True)


if __name__ == '__main__':
    unittest.main()
