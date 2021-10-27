#!/usr/bin/env python
"""Generating files that conform to the format required by fairseq-preprocess"""

import csv 
import argparse
from itertools import chain

def write_to_files(file_0, file_1, file_2):
    with open(file_0, "r") as source:
        my_data = csv.reader(source, delimiter = "\t")

        grapheme_list = [] #list of spelling: column 0 
        phoneme_list = [] #list of transcription: column 1

        for spelling, transcription in my_data: 
            grapheme_list.append(spelling)
            phoneme_list.append(transcription)

        with open(file_1, "w") as sink: 
            for item in grapheme_list:
                new_item = " ".join(list(chain.from_iterable(item)))
                print(new_item, file=sink)

        with open(file_2, "w") as sink: 
            for item in phoneme_list:
                print(item, file=sink)

def main(args: argparse.Namespace) -> None:
    write_to_files(args.train_data, "train.ice.g", "train.ice.p")
    write_to_files(args.dev_data, "dev.ice.g", "dev.ice.p")
    write_to_files(args.test_data, "test.ice.g", "test.ice.p")



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("train_data", help="training data file")
    parser.add_argument("dev_data", help="validation data file")
    parser.add_argument("test_data", help="testing data file")
main(parser.parse_args())

