"""This script generates a new file by substituting values in your base template

"""
import argparse
import json


def replace_all(text, dic):
    for i, j in dic.items():
        if isinstance(j, list):
            j = json.dumps(j)
        text = text.replace(i, j)
    return text


def read_and_generate(path, key_vals, prefix, suffix, ext):
    reading_file = open(path, "r")

    new_file_content = ""
    for line in reading_file:
        new_line = replace_all(line, key_vals)
        new_file_content += new_line
    reading_file.close()

    writing_file = open("{}_{}.{}".format(prefix, suffix, ext), "w")
    writing_file.write(new_file_content)
    writing_file.close()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "base_template_path", help="path to input base template for key value replacement")
    parser.add_argument(
        "output_file_prefix", help="prefix of the output file name")
    parser.add_argument(
        "output_file_suffix", help="suffix of the output file name")
    parser.add_argument(
        "output_file_extension", help="extension of the output file")
    parser.add_argument('--infile', nargs=1,
                        help="JSON file with key value mappings to replace",
                        type=argparse.FileType('r'))
    arguments = parser.parse_args()
    mappings = json.load(arguments.infile[0])
    read_and_generate(arguments.base_template_path, mappings,
                      arguments.output_file_prefix, arguments.output_file_suffix, arguments.output_file_extension)


main()
