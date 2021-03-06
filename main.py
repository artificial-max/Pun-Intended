#!/usr/bin/env python3
import sys
import argparse
from SearchEngine import SearchEngine

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description='Helps you build puns and lyrics')
    parser.add_argument('--vecs', type=str, default="glove.6B.100d.txt", help="Path to Glove/word2vec file (default: %(default)s)")
    parser.add_argument('--combo', type=str, default="sum", help="Combination method {sum|prod|inter} (default: %(default)s)")
    parser.add_argument('--rhyme', action="store_true", help="Restrict phonological matches to rhymes")
    parser.add_argument('--ortho', action="store_true", help="Use orthographic matches instead of phonological ones")
    parser.add_argument('--sound_like', type=str, help="Specify 'sounds-like' word")
    parser.add_argument('--means', type=str, help="Specify 'meaning' word")
    cmd_args = parser.parse_args()

    print("Hello and welcome to the pun aid!")
    se = SearchEngine(1000, cmd_args.vecs, cmd_args.combo)
    print(cmd_args.ortho)

    if cmd_args.ortho and cmd_args.rhyme:
        print('Looking for both orthographic matches and rhyming matches is not possible. Please choose one!')
        sys.exit()

    while True:

        query = input("Start search: \"Sounds like x\" \"Has to do with y\":\n> ")
        query = query.split()

        if not query:
            break

        elif len(query) != 2:
            print("Sorry, you need to provide two arguments!")
            continue
        else:

            print(se.execute_query(query[0], query[1], cmd_args.ortho, cmd_args.rhyme))
