import os
from tqdm.contrib.concurrent import process_map

mpii_root = "/data/junyan/MPIIGaze"

subjects = [os.path.join(args.mpii_root, "Data", "Original", 'p{:02d}/'.format(_i)) for _i in range(0, 15)]

def handle(subject):
    subject_id, subject_path = subject
    os.system(f"python GenerateMPIIH5Dataset.py --augment_dataset --mpii_root {mpii_root} --subject-path {subject_path} --subject-id {subject_id}")    


process_map(handle, list(enumerate(subjects)), max_workers=10)

