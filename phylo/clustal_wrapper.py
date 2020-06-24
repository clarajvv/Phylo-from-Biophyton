import os

from Bio.Align.Applications import ClustalwCommandline

class ClustalWrapper:
    def __init__(self, clustal_exe_path):
        self.clustalw_exe = clustal_exe_path

    def generate_alignment_tree(self, fasta_file):
        clustalw_cline = ClustalwCommandline(self.clustalw_exe, infile=fasta_file, seqnos="ON")
        assert os.path.isfile(self.clustalw_exe), "Clustal W executable missing"
        stdout, stderr = clustalw_cline()
