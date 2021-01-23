# Prepare the receptor using the pdb structure of the receptor and the mol2 file of the reference ligand/substrate
popdb2receptor -pdb oph.pdb -site_residue

# Generate 50 docking poses of the 1000 conformers of a ligand/substrate 
fred -receptor receptor.oeb.gz -dbase paraoxon-conformers.mol2 -dock_resolution High -num_poses 50 -score_tag -annotate_scores -save_component_scores

# Optimize the docked poses.
scorepose -receptor receptor.oeb.gz -in fred_docked_structure.oeb.gz -prefix opt -optimize Standard -sort_poses true -annotate -component_scores -score_tag -annotate_scores

# The generated docked pose could be found in the subdirectory: docked-poses
