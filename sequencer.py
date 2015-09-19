__author__ = 'tony'
import sys
class Sequence:
    WEIGHTS = {'A':131.2, 'C': 289.2,'G':329.2, 'T':304.2}
    def __init__(self, sequence=""):
        assert Sequence.is_valid(sequence),"Sequence should only contain A, C, G and T"
        self.nucleotides = sequence.upper()

    @staticmethod
    def is_valid(nucleotides):
        upper = nucleotides.upper() // convert all genome chars to upper case
        
        is_valid  = True;
        for c in upper:
                is_valid = is_valid and c in Sequence.WEIGHTS
        return is_valid

    @property
    def nucleotides(self):
        return self.nucleotides

    def get_weight(self):
        return Sequence.calculate_weight(self)

    @staticmethod
    def calculate_weight(sequence):
        weight= 0
        for c in sequence.nucleotides:
            weight+=Sequence.WEIGHTS[c]
        return weight

if __name__=="__main__":
    sequence = Sequence("GATTACCA")
    print(sequence.get_weight())
