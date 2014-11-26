import re
import sys
import yaml
import pprint
import requests

from collections import defaultdict

requirements_regex = re.compile(r'(?:The\s)?([A-Za-z]+)\s(?:property\s)?is\srequired') 
parse_required = lambda text: requirements_regex.findall(text)

sub_dict = lambda d, *args: {arg:d[arg] for arg in args}

def required_params(url, **kwargs):
	r = requests.get(url, **kwargs)
	return parse_required(r.text)

extract_result_headers = lambda data: map(lambda d: sub_dict(d, 'name', 'headers'), data['resultSets'])

def result_headers(url, **kwargs):
    r = requests.get(url, params=params)
    r.raise_for_status()
    return extract_result_headers(r.json())

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
    parser.add_argument('-p', '--params',
        nargs='?',
        action='store',
        dest='get_params',
        choices=('list', 'dict'),
        const='list',
        help='Get required parameters from list of URLs'
    )
    args = parser.parse_args()

    # input_ = yaml.load(args.infile)  
    # yaml.safe_dump(input_, args.outfile, default_flow_style=False)

    # exit(0)

    if args.get_params is not None:
        urls = yaml.load(args.infile)  

        resources = []
        for url in urls:
            params = required_params(url)
            if args.get_params == 'dict':
                params = dict.fromkeys(params)
            resources.append(dict(url=url, params=params))

        yaml.safe_dump(resources, args.outfile, default_flow_style=False)
        exit(0)

    resources = yaml.load(args.infile)

    for resource in resources:
        url = resource['url']
        params = resource['params']
        resource['results'] = result_headers(url, params=params)
        resource['params'] = resource['params'].keys()

    yaml.safe_dump(resources, args.outfile, default_flow_style=False)
