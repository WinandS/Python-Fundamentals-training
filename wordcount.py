from os.path import join
import argparse


def add_to_dict(key, dictionary):
    if key in dictionary:
        dictionary[key] += 1
    else:
        dictionary[key] = 1
    return dictionary


def count(input_file):
    dictionary = {}
    for line in input_file:
        for word in line.split():
            dictionary = add_to_dict(word, dictionary)
    return dictionary


def print_top(number, dictionary):
    sorted_values = dictionary.values()
    sorted_values.sort(reverse=True)
    # print(sorted_values)
    new_dict = {key: value for key, value in dictionary.items() if value in sorted_values[:number]}
    print_dict(new_dict)


def print_dict(dictionary):
    for key, value in dictionary.items():
        print "{key} : {value}".format(key=key, value=value)

parser = argparse.ArgumentParser()
parser.add_argument("--count", "-c", action="store_true", default=False)
parser.add_argument("--topcount", "-tc", action="store_true", default=False)
parser.add_argument("file", type=str)
args = parser.parse_args()


with open(args.file, 'r') as inf:
    my_dict = count(inf)
    if args.count:
        print_dict(my_dict)
    elif args.topcount:
        print_top(20, my_dict)
    else:
        print("No action defined.")
