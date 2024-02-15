"""
Podcast Downloader

Attempts to download every episode of a podcast in a given
RSS feed.


Usage:

python pod_dl.py -u [URL]

Optionally, you can also provide the -t argument to return only the podcast
titles without actually downloading anything.
"""

import sys
import argparse


import feedparser
import requests

def dl_with_requests(link, filename):
    r2 = requests.get(link)
    #print(type(r2.content))
    #print(sys.getsizeof(r2.content))
    with open(filename, "wb") as f:
        f.write(r2.content)
        #print(sys.getsizeof(f))

def pod_dl(url, titles):

    # Check to see if RSS URL can be accessed and, if so, get the feed
    # using requests.  If not, return the http error code and end the program.
    try:
        r = requests.get(url)
    except Exception as e:
        print(f"There was an error: {e}.\n\nPlease ensure that a valid URL"
          " was provided.")
        sys.exit()
        
    status = r.status_code
    if status == 200:
        pass
    else:
        print("There was a problem accessing the RSS feed.  HTTP Status "
          f"code {status} was returned.  Please ensure that the RSS URL"
          " provided is accessable from a web browser.")
        sys.exit()
        
    # Parse the feed with feedparser
    d = feedparser.parse(r.text)
    
    # check to see if titles argument is True.  If so, print a list of titles
    # and end the program
    if titles is True:
        for item in d.entries:
            print(item.title)
        sys.exit()
    else:
        pass
    
    # Download all episodes
    
    for item in d.entries:
        for link in item.enclosures:
            pod_url = link.get("href")
            print(pod_url)
            filename = item.title + ".mp3"
            filename = filename.replace(":", "-")
            filename = filename.replace(" ", "_")
            filename = filename.replace("/", "_")
            filename = filename.replace("?", "_")
            #print(filename)
            print(f"Now downloading: {filename}")
            dl_with_requests(pod_url,filename)
    
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