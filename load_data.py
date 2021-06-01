# coding: utf-8

import os
import sys
import json


def load_data(file_path):
    print("Loading data from {}".format(file_path))
    with open(file_path, "r") as f:
        data = [json.loads(l.strip()) for l in f]
    print("Load {} dialogues".format(len(data)))
    print("Sample dialogue:")
    for key, value in data[0].items():
        print("{}: {}".format(key, value))


if __name__ == "__main__":
    data_dir = "./data"
    filename_list = ["train.json", "valid.json", "test.json"]
    for filename in filename_list:
        file_path = os.path.join(data_dir, filename)
        load_data(file_path)
