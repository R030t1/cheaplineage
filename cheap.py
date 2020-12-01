#!/usr/bin/env python3
import os, sys
import requests, html.parser
from pprint import pprint

def main() -> int:
    d = requests.get('https://download.lineageos.org/').text

    for l in d.split('\n'):
        if 'device-link' not in l:
            continue
        pprint(l)

    return 0

if __name__ == '__main__':
    sys.exit(main())
