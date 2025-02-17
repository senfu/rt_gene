#!/usr/bin/env python

# Licensed under Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International
# (https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode)

from __future__ import print_function, division, absolute_import
import sys
sys.path.append("/home/student/dms/rt_gene/rt_gene/src/rt_gene")

import download_tools


if __name__ == '__main__':
    # download_tools.download_gaze_tensorflow_models()
    download_tools.download_gaze_pytorch_models()
    # download_tools.download_blink_tensorflow_models()
    download_tools.download_blink_pytorch_models()
    download_tools.download_external_landmark_models()

