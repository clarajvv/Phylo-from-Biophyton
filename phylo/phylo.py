import Phylo, sys
from io import StringIO

treeBC = Phylo.read("files/BetaCasein.dnd", "newick")
treePPN = Phylo.read("files/PyrimidinePurineNucleosidePhosphorylase.dnd", "newick")


# maneras de dibujar el árbol
# print(treeBC)
# Phylo.draw_ascii(treeBC)
# treeBC.rooted=True
# Phylo.draw(treeBC)
# Phylo.write(treeBC, sys.stdout, "phyloxml")

def drawTree(tree, type):
    if type == 1:
        print(tree)
    elif type == 2:
        Phylo.draw_ascii(tree)
    elif type == 3:
        tree.rooted = True
        Phylo.draw(tree)
    elif type == 4:
        Phylo.write(tree, sys.stdout, "phyloxml")


# dibujar una parte solo con string:
fragment = StringIO(
    "((tr|A0A0D9QY03|A0A0D9QY03_CHLSB:0.00189,tr|A0A2K5U2F4|A0A2K5U2F4_MACFA:0.00696):0.03122,(sp|Q9GKK3|CASB_HORSE:0.16524,sp|Q9TSI0|CASB_BUBBU:0.21869));")
partialTree = Phylo.read(fragment, "newick")
drawTree(partialTree, 3)

#seleccionar rama o clade
treePPN.clade[0,1,1,1]

#terminales y no terminales:
def terminales(tree):
    return tree.get_terminals(), tree.get_nonterminals()

#terminales(treeBC)
#terminales(treePNN)

#common ancestor mal
#treePPN.common_ancestor({"name": "sp|Q9KKY0|PPNP_VIBCH"},{"name":"sp|A0KK62|PPNP_AERHH"})

#cambio a otros archivos por problemas de biopython
smpBC=Phylo.read("files/BCsimpl.dnd", "newick")
smpPPN=Phylo.read("files/PPNsimpl.dnd", "newick")