from phylo.clustal_wrapper import ClustalWrapper


if __name__ == '__main__':
    clustalWPath = "D:\\clustalForBiopython\\CLustalW2.exe"

    clustalWrapper = ClustalWrapper(clustalWPath)

    ##Example 1
    clustalWrapper.generate_alignment_tree(("proteins\\BetaCasein.fasta"))
    ##Example 2
    clustalWrapper.generate_alignment_tree("proteins\\PyrimidinePurineNucleosidePhosphorylase.fasta")
