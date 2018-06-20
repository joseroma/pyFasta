from Bio import SeqIO

archive_1 = 'archives/rosalind_grph.txt'
archive_2 = 'archives/rosalind_lcsm.txt'


class FASTA:

    def __init__(self, file_name):

        self.fich = file_name

    def read_fasta_file_as_list_of_pairs(self):

        f = open("results/result1.txt", "w")
        f.write('Fasta --> Pairs   \n\n\n [')
        for record in SeqIO.parse(self.fich, 'fasta'):
            f.write('[ '+str(record.id)+',' + str(record.seq) + ' ]' + "\n")
        print("You can see the results in /results/result1")
        f.write("]")
        f.close()
        return record.id

    def read_fasta_file_as_dictionary(self):

        Dictionary = {}

        for sequence in SeqIO.parse(self.fich, 'fasta'):

            ident = sequence.id
            Dictionary.setdefault(ident, [])
            Dictionary[ident].append(sequence.seq)
            f = open("results/result2.txt", "w")

        for result, values in Dictionary.items():
            f.write(str(result))
            f.write(str(values))
        print("You can see the results in /results/result2")

        f.close()



pares = FASTA(archive_1)
#print('Fasta --> Pairs ')
pares.read_fasta_file_as_list_of_pairs()
#print(type(pares))
#print("<class '__main__.Fasta'>"==str(type(pares)))

dic = FASTA(archive_2)
#print('Fasta --> Dictionary (view archive)')
pares.read_fasta_file_as_dictionary()

