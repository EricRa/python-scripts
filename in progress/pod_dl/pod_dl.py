"""
Podcast Downloader

Attempts to download every episode of a podcast in a given
RSS feed.

"""

import sys
import argparse

import feedparser
import requests
from icecream import ic

# rss test link
test_rss = ("https://www.omnycontent.com/d/playlist/e73c998e"
  "-6e60-432f-8610-ae210140c5b1/6a4a4e0f-8e8d-40e5-9d99-ae8601259"
  "b78/0f0d9558-3e6e-4af7-971b-ae860127535c/podcast.rss")
    
ic(test_rss)

def pod_dl(url, titles):
    pass

# argument parser

parser = argparse.ArgumentParser(
    prog="podcast downloader",
    description="A password generator using the Python secrets module",
    epilog=""
)
parser.add_argument(
    "-u",
    "--url",
    help="URL of the RSS feed"
)
parser.add_argument(
    "-t",
    "--titles",
    action="store_true",
    default=False,
    help=("Will attempt to return the titles of all podcast episodes "
      "in the feed without actually downloading the episodes")
)

args = parser.parse_args()

# Run pod_dl function with given command line arguments
pod_dl(**vars(args))