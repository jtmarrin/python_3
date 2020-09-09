#!/usr/bin/env python3

# script to search dirs recursively and give a tree like output

import os

# traverse root dir, and list as dirs and files as files
for root, dirs, files in os.walk("."):
    path = root.split(os.sep)
    print((len(path) -1) * '---', os.path.basename(root))
    for file in files:
        print(len(path) * '___', file)

