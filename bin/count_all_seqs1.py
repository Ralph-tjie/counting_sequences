#!/usr/bin/env python

import os
import seq_utils
import sys

def count_seqs1(path):
    filenames = sorted (os.listdir(path))
    os.chdir(path)

    for filex in filenames:
        input_file = open(filex)
        seq_count = seq_utils.count_seqs(input_file)
        print seq_count,"in",filex


if len(sys.argv) != 2:
        sys.exit("Usage: count_all_seqs1.py <filenames>")

print count_seqs1(sys.argv[1])


