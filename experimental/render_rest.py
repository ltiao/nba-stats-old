from __future__ import print_function

import sys
import yaml
import pprint

from jinja2 import Environment, FileSystemLoader

if __name__ == '__main__':

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('infile', 
        nargs='?',
        type=argparse.FileType('r'),
        default=sys.stdin
    )
    parser.add_argument('outfile',
        nargs='?',
        type=argparse.FileType('w'),
        default=sys.stdout
    )
    args = parser.parse_args()

    resources = yaml.load(args.infile)

    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('required_params.rst')

    print(template.render(resources=resources), file=args.outfile)
