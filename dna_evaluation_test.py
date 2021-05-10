import unittest

import is_mutant


class DnaValidationTest(unittest.TestCase):
    def should_identify_horizontal_sequences_and_mark_as_mutant_if_find_more_than_one(self):
        dna_with_two_horizontal_sequences = {"ATAAAA",
                                             "CTGTGC",
                                             "TTGTGT",
                                             "AGAAGG",
                                             "CCCCTA",
                                             "TCACTG"}
        dna_is_mutant = is_mutant.is_mutant_dna(dna_with_two_horizontal_sequences)
        self.assertEqual(dna_is_mutant, True)


if __name__ == '__main__':
    unittest.main()
