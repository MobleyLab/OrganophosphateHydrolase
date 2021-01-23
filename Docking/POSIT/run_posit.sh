# Prepare the receptor using the pdb structure of the receptor and the mol2 file of the reference ligand/substrate
receptor_setup -protein oph.pdb -bound_ligand reference.mol2

# Dock the 1000 conformers of the ligand (here the substrate paraoxon) using posit
posit -receptor receptor.oeb.gz -dbase paraoxon-conformers.mol2

# The generated docked pose could be found in the subdirectory: docked-pose
