#!/usr/bin/env python

import sys

def main():
    if len(sys.argv) != 4:
        print("Usage: slice_list.py <comma_separated_list> <start_index> <end_index>")
        sys.exit(1)

    input_list = sys.argv[1].split(',')
    start_index = int(sys.argv[2])
    end_index = int(sys.argv[3])

    sliced_list = input_list[start_index:end_index + 1]

    print(','.join(sliced_list))

if __name__ == "__main__":
    main()

