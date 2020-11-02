import argparse
import json
import os
import urllib.parse
import urllib.request


def download_url(_url, _name, output_dir=''):
    output = os.path.join(output_dir, _name)
    if not os.path.isfile(output):
        urllib.request.urlretrieve(_url, filename=output)
    return output


parser = argparse.ArgumentParser()
parser.add_argument('-f', '--filepath', help='Enter the Filepath to file contains with links', required=True)
args = parser.parse_args()
filepath = args.filepath
file = open(filepath, 'r')

with open(filepath) as f:
    links = json.load(f)

for link in links:
    name = link['title']
    url = link['url']
    print(f'Downloading {name} from {url}.')
    download_url(url, name, 'output')
    print(f'Finished Downloading {name} from {url}.')

print('DONE!')
