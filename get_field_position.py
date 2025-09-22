#!/usr/bin/env python3

from sys import argv as args


DEFAULT_SEPARATOR = ','

with open(args[2], 'r') as f:
    for line in f:
        fields = line.split(DEFAULT_SEPARATOR)
        for count, field in enumerate(fields):
            if field.strip() == args[1]:
                print(count + 1)
                break
        break

