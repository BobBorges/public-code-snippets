#!/usr/bin/env python3
import os, json

def main():
    corpus_files = os.listdir('corpus')
    bag = {}

    for corpus_file in corpus_files:
        with open(f'corpus/{corpus_file}', 'r') as txtfile:
            txt_lines = txtfile.readlines()
            for line in txt_lines:
                line = line.strip()
                words = line.split(' ')
                for word in words:
                    if word not in bag:
                        bag[word] = 1
                    else:
                        bag[word] += 1

    print(bag)


if __name__ == '__main__':
	main()
