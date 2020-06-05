from phylo.ClustalWrapper import ClustalWrapper

if __name__ == '__main__':
    
    clustalWPath = "D:\clustalForBiopython\CLustalW2.exe"

    clustalWrapper = ClustalWrapper(clustalWPath)
    ##Test 1
    clustalWrapper.generate_alignment_tree("proteins/opuntia.fasta")

    ##Example 1
    clustalWrapper.generate_alignment_tree(("proteins/BetaCasein.fasta"))
    ##Example 2
    clustalWrapper.generate_alignment_tree("proteins/PyrimidinePurineNucleosidePhosphorylase.fasta")