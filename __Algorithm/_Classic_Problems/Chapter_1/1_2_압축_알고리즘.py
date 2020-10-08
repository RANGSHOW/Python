# sys.getsizeof() : 객체가 소비하고 있는 바이트(byte)를 알려준다.
class CompressedGene:
    def __init__(self, gene: str) -> None:
        self._compress(gene)
        
    def _compress(self, gene: str) -> None:
        self.bit_string: int = 1
            for nucleotide in gene.upper():
                self.bit_string <<= 2
                