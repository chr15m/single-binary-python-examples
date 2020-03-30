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
@click.option('--echo', '-s', help='Output some text to the console.')
@click.option('--fetch-title', '-f', help='Fetch a web URL and show the title of the page.')
@click.option('--arp', '-a', is_flag=True, help='Print the arp table of this computer.')
def main(echo, fetch_title, arp):
    if echo:
        print("Your message:", echo)
    if fetch_title:
        titles = re.findall("<title>(.*?)</title>", str(urlopen(fetch_title).read()), re.IGNORECASE | re.MULTILINE)
        if titles:
            print(titles[0])
        else:
            print("No title found.")
    if arp:
        print(sh.arp("-a").rstrip())
    if not (echo or fetch_title or arp):
        print("You didn't specify any options. Use --help to get help.")

if __name__ == "__main__":
    main()
