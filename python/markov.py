#!/usr/bin/env python

# Write a Markov text generator, [markov.py](python/markov.py). Your program should be called from the command line with two arguments: the name of a file containing text to read, and the number of words to generate. For example, if `chains.txt` contains the short story by Frigyes Karinthy, we could run:

# ```bash
# ./markov.py chains.txt 40
# ```

# A possible output would be:

# > show himself once more than the universe and what I often catch myself playing our well-connected game went on. Our friend was absolutely correct: nobody from the group needed this way. We never been as the Earth has the network of eternity.

# There are design choices to make; feel free to experiment and shape the program as you see fit. Jeff Atwood's [Markov and You](http://blog.codinghorror.com/markov-and-you/) is a fun place to get started learning about what you're trying to make.

"""This module contains a code example related to
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
Copyright 2015 Allen Downey
License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division


import sys
import random

def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.
    fp: open file object
    The python is lazy. It never go back an reread the contents. So this function can let us skip the Gutenberg header.
    """
    for line in fp:
        if line.startswith('*END*THE SMALL PRINT!'):
            break

def shift(t, word):
    """Forms a new tuple by removing the head and adding word to the tail.
    t: tuple of strings
    word: string
    Returns: tuple of strings
    """
    return t[1:] + (word,)

class Markov:
    """Encapsulates the statistical summary of a text."""

    def __init__(self):
        self.suffix_map = {}        # map from prefixes to a list of suffixes
        self.prefix = ()            # current tuple of words

    def process_file(self, filename, order=2):
        """Reads a file and performs Markov analysis.
        filename: string
        order: integer number of words in the prefix
        Returns: map from prefix to list of possible suffixes.
        """
        fp = open(filename)   #type is _io.TextIOWrapper
        """If the txt has Gutenberg header
        skip_gutenberg_header(fp)
        """

        for line in fp:
            for word in line.rstrip().split():
                self.process_word(word, order)

    def process_word(self, word, order=2):
        """Processes each word.
        word: string
        order: integer
        During the first few iterations, all we do is store up the words;
        after that we start adding entries to the dictionary.
        """
        if len(self.prefix) < order:
            self.prefix += (word,)
            return

        try:
            self.suffix_map[self.prefix].append(word)
        except KeyError:
            # if there is no entry for this prefix, make one
            self.suffix_map[self.prefix] = [word]

        self.prefix = shift(self.prefix, word)

    def random_text(self, n=100):
        """Generates random wordsfrom the analyzed text.
        Starts with a random prefix from the dictionary.
        n: number of words to generate
        """
        # choose a random prefix (not weighted by frequency)
        start = random.choice(list(self.suffix_map.keys()))

        for i in range(n):
            suffixes = self.suffix_map.get(start, None)   #If there is no key then return None.
            if suffixes == None:
                # if the prefix isn't in map, we got to the end of the
                # original text, so we have to start again.
                self.random_text(n-i)
                return

            # choose a random suffix
            word = random.choice(suffixes)
            print(word, end=' ')
            start = shift(start, word)


def main(script, filename, n=100, order=2):
    try:
        n = int(n)
        order = int(order)
    except ValueError:
        print('Usage: %d filename [# of words] [prefix length]' % script)
    else:
        markov = Markov()
        markov.process_file(filename, order)
        markov.random_text(n)


if __name__ == '__main__':
    main(*sys.argv)


