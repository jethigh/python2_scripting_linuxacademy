import argparse

parser = argparse.ArgumentParser()
parser.add_argument('filename', help='file to read')
parser.add_argument('--limit', '-l', type=int, help='Number of lines to read')
args = parser.parse_args()

try:
    file = open(args.filename)
except IOError as err:
    print('Nie znalazlem pliku: ' + str(args.filename))
else:
    # Tutaj ciekawe
    # zamiast with open(args.filename) as file:
    # jest with file, i to with samo zamknie polaczenie
    # ale mozna by bez with i zamknac w finally:    
    with file:
        lines = file.readlines()
        if args.limit:
            lines = lines[:args.limit]
        for line in lines:
            print line,
finally:
    print('Koncze prace ')
