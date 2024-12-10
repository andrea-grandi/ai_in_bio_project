#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 14:23:18 2024

@author: andreagrandi
"""

import os
import shutil


def prune_subdirectories(base_dir, keep_dirs):
    # Iterate through each subdirectory in the base directory
    for root_dir in os.listdir(base_dir):
        root_path = os.path.join(base_dir, root_dir)
        if os.path.isdir(root_path):
            print(f"Processing: {root_path}")
            # List all subdirectories inside the current root directory
            for sub_dir in os.listdir(root_path):
                sub_path = os.path.join(root_path, sub_dir)
                # If the subdirectory isn't in the keep list, delete it
                if os.path.isdir(sub_path) and sub_dir not in keep_dirs:
                    print(f"Deleting: {sub_path}")
                    shutil.rmtree(sub_path)
                elif os.path.isdir(sub_path):
                    print(f"Keeping: {sub_path}")


base_directory = "nulnsseg"
directories_to_keep = ['tissue images', 'mask binary without border', 'label masks modify']

prune_subdirectories(base_directory, directories_to_keep)