import csv

from sentence_transformers import InputExample

import constants as c


def create_samples(csv_file, type=0, size=None):
    samples = []
    with open(c.DATA_DIR + csv_file) as test_set:
        sample_reader = csv.DictReader(test_set)
        
        # type 0: use InputExample
        if type == 0:
            samples = [
                InputExample(
                    texts=[s[c.TOPIC_KP], s[c.ARG]],
                    label=int(s[c.LABEL])
                ) for s in sample_reader
            ]

        # type 1: create a standard dictionary
        else:
            samples = [
                {
                    c.ARG: s[c.ARG],
                    c.TOPIC_KP: s[c.TOPIC_KP],
                    c.LABEL: int(s[c.LABEL])
                } for s in sample_reader
            ]

    if size:
        samples = samples[:size]

    return samples