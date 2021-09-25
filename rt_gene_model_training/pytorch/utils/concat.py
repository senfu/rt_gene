import h5py
import os.path as osp
import glob

mpii_root = "/data/junyan/MPIIGaze"
with h5py.File(osp.join(mpii_root, 'mpii_dataset.hdf5'), mode='w') as h5fw:
    for h5name in glob.glob(osp.join(mpii_root, 'mpii_dataset_*.hdf5')):
        print(h5name)
        h5fr = h5py.File(h5name, 'r')
        for obj in h5fr.keys():
            h5fr.copy(obj, h5fw)
print("done")
