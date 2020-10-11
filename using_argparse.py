import argparse

parser = argparse.ArgumentParser()
parser.add_argument('filename', help='file to read')
parser.add_argument('--limit', '-l', type=int, help='Number of lines to read')
args = parser.parse_args()

with open(args.filename) as file:
    lines = file.readlines()
    if args.limit:
        lines = lines[:args.limit]
    for line in lines:
        print line,
