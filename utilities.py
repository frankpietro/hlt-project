import csv
import numpy as np
import os

from sentence_transformers import InputExample

import constants as c


def create_samples(csv_file, size=None):
    samples = []
    with open(c.DATA_DIR + csv_file) as test_set:
        sample_reader = csv.DictReader(test_set)
        
        samples = [
            InputExample(
                texts=[s[c.TOPIC_KP], s[c.ARG]],
                label=int(s[c.LABEL])
            ) for s in sample_reader
        ]
    
    if size:
        samples = samples[:size]

    return samples


def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def empty_folder(path):
    # if folder does not exist, create it
    if not os.path.exists(path):
        os.makedirs(path)
    
    # remove all files in folder
    for file in os.listdir(path):
        os.remove(os.path.join(path, file))


def is_model_present(model_name):
    p = c.MODELS_DIR + model_name
    # return true if there are files in the folder
    return os.path.exists(p) and len(os.listdir(p)) > 0