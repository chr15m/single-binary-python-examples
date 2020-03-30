#!usr/bin/env python
# coding=utf8

from __future__ import print_function

import re

try:
    from urllib2 import urlopen
except:
    from urllib.request import urlopen

import click
import sh

@click.command()
@click.option('--say', '-s', help='Output some text to the console.')
@click.option('--fetch-title', '-f', help='Fetch a web URL and show the title of the page.')
def main(say, fetch_title):
    if say:
        print("Your message:", say)
    if fetch_title:
        titles = re.findall("<title>(.*?)</title>", str(urlopen(fetch_title).read()), re.IGNORECASE | re.MULTILINE)
        if titles:
            print(titles[0])
        else:
            print("No title found.")
    if not (say or fetch_title):
        print("You didn't specify any options. Use --help to get help.")

if __name__ == "__main__":
    main()
