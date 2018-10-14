import os
import sys

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

def get_base_dir():
    return ROOT_DIR


def get_abs_path(filename):
    return os.path.join(ROOT_DIR, filename)