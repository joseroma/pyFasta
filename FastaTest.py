import unittest


from Fasta import FASTA


class TestMethods(unittest.TestCase):

    def test_should_raise_an_exception_dictionary_bad_routing(self):
        self.fasta = FASTA('/ruta_equivocada')
        with self.assertRaises(Exception):
            self.fasta.read_fasta_file_as_dictionary()

    def test_should_raise_an_exception_pairs_bad_routing(self):
        self.fasta = FASTA('/ruta_equivocada')
        with self.assertRaises(Exception):
            self.fasta.read_fasta_file_as_list_of_pairs()

    def test_should_ok_first_ID(self):
        self.fasta = FASTA('archives/rosalind_grph.txt')
        rec = self.fasta.read_fasta_file_as_list_of_pairs()
        print(str(rec[0:14]))
        self.assertEqual('Rosalind_2869', str(rec[0:14]))

    def test_should_result_type_1(self):
        self.fasta = FASTA('archives/rosalind_grph.txt')
        self.fasta.read_fasta_file_as_list_of_pairs()
        print(str(type(self.fasta)))
        self.assertEqual("<class 'reader_fasta.Fasta'>", str(type(self.fasta)))

    def test_should_result_type_2(self):
        self.fasta = FASTA('archives/rosalind_grph.txt')
        self.fasta.read_fasta_file_as_dictionary()
        print(str(type(self.fasta)))
        self.assertEqual("<class 'reader_fasta.Fasta'>", str(type(self.fasta)))

    def tearDown(self):
        print("Test passed correctly")