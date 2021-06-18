"""This script generates a new file by substituting values in your base template

"""
import argparse
import json
from typing import Any, Dict


def replace_all(text: str, dic: Dict[str, Any]) -> str:
    for i, j in dic.items():
        if isinstance(j, list):
            j = json.dumps(j)
        text = text.replace(i, j)
    return text


def read_and_generate(path: str, key_vals: Dict[str, Any], file_name: str, content_builder: str = str()) -> None:
    reading_file = open(path, "r")

    for line in reading_file:
        new_line = replace_all(line, key_vals)
        content_builder += new_line
    reading_file.close()

    writing_file = open("{}".format(file_name), "w")
    writing_file.write(content_builder)
    writing_file.close()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "base_template_path", help="path to input base template for key value replacement", type=str)
    parser.add_argument(
        "output_file_name", help="output file name and its extension", type=str)
    parser.add_argument('mappings_file', nargs=1,
                        help="JSON file with key value mappings to replace",
                        type=argparse.FileType('r'))
    arguments = parser.parse_args()
    mappings = json.load(arguments.mappings_file[0])
    read_and_generate(arguments.base_template_path, mappings,
                      arguments.output_file_name)


main()
