import argparse
import os
from tqdm.contrib.concurrent import process_map

parser = argparse.ArgumentParser(description='Estimate gaze from images')
parser.add_argument('--mpii_root', type=str, required=True, nargs='?', help='Path to the base directory of MPII')
parser.add_argument('--augment_dataset', action='store_true', help="Whether to augment the dataset with predefined transforms")
parser.add_argument('--compress', action='store_true', dest="compress")
parser.add_argument('--no-compress', action='store_false', dest="compress")
parser.set_defaults(compress=False)
args = parser.parse_args()
subjects = [os.path.join(args.mpii_root, "Data", "Original", 'p{:02d}/'.format(_i)) for _i in range(0, 15)]

def handle(subject):
    subject_id, subject_path = subject
    os.system(f"python GenerateMPIIH5Dataset.py --augment_dataset --compress --mpii_root /data/junyan/MPIIGaze --subject-path {subject_path} --subject-id {subject_id}")    


process_map(handle, list(enumerate(subjects)), max_workers=10)

