import numpy
import openeye.oechem
from openeye.oechem import *

def rmsd_cluster(input, ref, output, clusters):
    """
    input is str of file to read in containing strucutres
    ref apparently doesn't matter, but I used the same argument as input
    output is file str to output structures to
    clusters is an int specifying the number of clusters to make
    """
    ifs = oemolistream()
    if not ifs.open(input):
        OEThrow.Fatal("Unable to open %s for reading" % input)
    poses = list()
    mol = OEMol()
    while OEReadMolecule(ifs, mol):
        mol_copy = OEMol(mol)
        #print(dir(mol_copy))
        #print(mol_copy.NumConfs())
        for conf in mol_copy.GetConfs():
            poses.append(conf)
    ifs.close()
    print("%d poses read" % len(poses))

    # Create a list of centroids, starting with first molecule.
    centroids = list()

    # Make first pose our first centroid.
    centroids.append(poses.pop(0))
    if int(clusters) < len(poses):
        print("Will return %s poses..." % clusters)
    else:
        print("Will return %s poses..." % (len(poses)+1))
    while len(centroids) < int(clusters) and len(poses)>0:
        print(len(centroids))
        # Compute distance from all poses to closest centroid.
        min_rmsd = numpy.zeros([len(poses)])
        for (pose_index, pose) in enumerate(poses):
            centroids_rmsds = [OERMSD(pose, centroid) for centroid in centroids]
            min_rmsd[pose_index] = min(centroids_rmsds)
    # Find pose that is farthest away from all current centroids.
        farthest_pose_index = min_rmsd.argmax()
        print("Farthest pose is %d at %f A away from centroids" % (farthest_pose_index, min_rmsd[farthest_pose_index]))
    # Move farthest pose to centroids.
        centroids.append(poses.pop(farthest_pose_index))
    # Write out all centroids.
    ofs=oemolostream()
    if not ofs.open(output):
        OEThrow.Fatal("Unable to open %s for writing" % itf.GetString("-o"))
    for mol in centroids:
            #OEWritePDBFile(ofs, mol)
        OEWriteMolecule(ofs, mol)

    print("Done!")

    return 0

rmsd_cluster('poses.oeb.gz', 'poses.oeb.gz', 'poses.pdb', 50)
