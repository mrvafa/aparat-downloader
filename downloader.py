import os
import sys
import urllib.parse
import urllib.request


def get_name_from_url(url):
    url = url[url.rfind('/') + 1:]
    return urllib.parse.unquote(url)


def download_url(url, output_dir=''):
    output_dir = os.path.abspath(output_dir)
    url_head = url[:url.find('//')]
    url_body = urllib.parse.unquote(url[url.find('//'):])
    url = url_head + urllib.parse.quote(url_body)
    download_name = get_name_from_url(url)
    output = os.path.join(output_dir, download_name) if output_dir else download_name
    if not os.path.isfile(output):
        urllib.request.urlretrieve(url, filename=output)
    return output


if not os.path.isdir('output'):
    os.mkdir('output')

if not os.path.isfile('output.txt'):
    print('output.txt not found')
    sys.exit(1)

file = open('output.txt', 'r')

for line in file.readlines():
    line = line.strip()
    download_url(line, output_dir='output')

print('DONE!')
