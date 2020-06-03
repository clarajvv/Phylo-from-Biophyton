def read_multiFasta(protein_file):
    fastas = {}

    file = open(protein_file)

    for line in file:

        if (line[0] == ">"):
            head = line[1:]
            seq = ""

        else:
            line = line.rstrip("\r")
            seq += line.rstrip("\n")
            fastas[head] = seq

    return fastas

read_multiFasta("proteins/BetaCasein.txt")
read_multiFasta("proteins/PyrimidinePurineNucleosidePhosphorylase.txt")
