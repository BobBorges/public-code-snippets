#!/usr/bin/env python3
import os, json

def main():
    ### list all files in the corpus dir
    corpus_files = os.listdir('corpus')
    ### initialize empty dictionary 
    bag = {}

    ### create bag of words
    for corpus_file in corpus_files:                            # iterate over list of files
        with open(f'corpus/{corpus_file}', 'r') as txtfile:     # open each file for reading
            txt_lines = txtfile.readlines()                     # read each line to a list
            for line in txt_lines:                              # iterate over list of lines
                line = line.strip()                             # strip punctuation and returns
                words = line.split(' ')                         # split line by space -> list of words
                for word in words:                              # iterate over list of words
                    if word not in bag:                         # if word not in bag dictionary
                        bag[word] = 1                           # add it with value of 1
                    else:                                       # or else
                        bag[word] += 1                          # increment the existing val by 1

    print(bag)
    #sort by val
    #dump to a file


if __name__ == '__main__':
	main()
