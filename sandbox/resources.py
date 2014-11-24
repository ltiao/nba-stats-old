import re
import yaml
import pprint
import requests

from collections import defaultdict

requirements_regex = re.compile(r'(?:The\s)?([A-Za-z]+)\s(?:property\s)?is\srequired') 
parse_required = lambda text: requirements_regex.findall(text)

def required_params(url):
	r = requests.get(url)
	return parse_required(r.text)

if __name__ == '__main__':

	with open('resources.yml', 'r') as infile:
		urls = yaml.load(infile)

	temp = defaultdict(dict)

	for url in urls:
		temp[url]['required'] = required_params(url)

	pprint.pprint(temp)