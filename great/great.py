#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from sys import argv
from os import path
GREAT_COMMANDS =  {"great":"👍", "shit": "💩"}
def _main(args):
    m = GREAT_COMMANDS
    out = ' '.join(m.get(path.splitext(path.basename(i))[0], "") for i in args)
    print out

def main():
    _main(argv)

if __name__ == "__main__":
    main()

