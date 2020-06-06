import unittest
from phylo.clustal_wrapper import ClustalWrapper
import filecmp

class TestClustalWrapper(unittest.TestCase):

    def test_dndfile(self):
        clustalWPath = "D:\clustalForBiopython\CLustalW2.exe"
        clustalWrapper = ClustalWrapper(clustalWPath)
        clustalWrapper.generate_alignment_tree('..\\phylo\\proteins\\opuntia.fasta')
        isEqual = filecmp.cmp('..\\phylo\\test\\testFiles\\correctOpuntia.dnd', '..\\phylo\\proteins\\opuntia.dnd', shallow= False)
        self.assertTrue(isEqual)

if __name__ == '__main__':
    unittest.main()
