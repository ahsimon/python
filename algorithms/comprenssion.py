# Compression is the act of taking data and
# encoding it (changing its form) in such a way that it takes up less space. Decompression
# is reversing the process, returning the data to its original form

class CompressedGene:
    def __init__(self, gene: str) -> None:
        self.compress(gene)
        