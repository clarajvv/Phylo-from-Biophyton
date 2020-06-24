import Phylo, sys, copy
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

# drawTree(treeBC, 1)
# drawTree(treeBC, 2)
# drawTree(treeBC, 3)
# drawTree(treeBC, 4)
# drawTree(treePPN, 1)
# drawTree(treePPN, 2)
# drawTree(treePPN, 3)
# drawTree(treePPN, 4)


# dibujar una parte solo con string:
fragment = StringIO(
    "((tr|A0A0D9QY03|A0A0D9QY03_CHLSB:0.00189,tr|A0A2K5U2F4|A0A2K5U2F4_MACFA:0.00696):0.03122,(sp|Q9GKK3|CASB_HORSE:0.16524,sp|Q9TSI0|CASB_BUBBU:0.21869));")
partialTree = Phylo.read(fragment, "newick")
# drawTree(partialTree, 3)

#seleccionar rama o clade
# drawTree(treePPN.clade[0,1,1],3)
# drawTree(treeBC.clade[1,1,1], 3)

#terminales y no terminales:
def terminales(tree):
    return tree.get_terminals(), tree.get_nonterminals()

#terminales(treeBC)
#terminales(treePPN)

#common ancestor mal
#treePPN.common_ancestor({"name": "sp|Q9KKY0|PPNP_VIBCH"},{"name":"sp|A0KK62|PPNP_AERHH"})

#cambio a otros archivos por problemas de biopython
smpBC=Phylo.read("files/BCsimpl.dnd", "newick")
smpPPN=Phylo.read("files/PPNsimpl.dnd", "newick")

comunBC=smpBC.common_ancestor({"name":"A0A0D9QY03_CHLSB"}, {"name":"CASB_HORSE"})
comunPPN=smpPPN.common_ancestor({"name":"PPNP_RALSO"}, {"name":"PPNP_CUPNH"})

#colorear ramas de ancestros comunes
comunBC.color="#99ccff"
comunPPN.color="#ffcccc"

#drawTree(smpBC, 3)
#drawTree(smpPPN, 3)

#colorear con clade
smpBC=Phylo.read("files/BCsimpl.dnd", "newick")
smpPPN=Phylo.read("files/PPNsimpl.dnd", "newick")

#smpBC.clade[1,1,1].color="#99ccff"
#drawTree(smpBC,3)

#smpPPN.clade[0,1,0,0].color="#ffcccc"
#drawTree(smpPPN,3)

#path
#smpBC.get_path(name="G1R7Y4_NOMLE")
#smpPPN.get_path(name="PPNP_SHEON")

#trace and distances
# smpBC.trace("CASB_HORSE", "H2QPK9_PANTR")
#smpBC.distance("CASB_HORSE", "H2QPK9_PANTR")
# smpPPN.trace("PPNP_CUPNH", "PPNP_AERHH")

#count terminals
# smpPPN.count_terminals()
# smpBC.count_terminals()

#vamos a hacer métodos que modifican el árbol, así que lo copiamos
copPNN=copy.deepcopy(smpPPN)

# copPNN.collapse("PPNP_ECOLI")
# copPNN.collapse_all()
# copPNN.ladderize()



