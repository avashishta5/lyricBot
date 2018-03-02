#!/usr/bin/env python

# LyricBot
# To fetch song lyrics, obviously.
# Made by someone with waaay to much time on his hands.
# Started September 30, 2016.

import urllib2
import re
import time
while True:
    url = "http://search.azlyrics.com/search.php?q="
    query = raw_input("Enter Song Name: ")
    start = time.time()
    query = query.replace(" ", "+")
    query.strip()
    req_1 = urllib2.Request(url+query)
    resp_1 = urllib2.urlopen(req_1)
    html_1 = resp_1.read()
    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str(html_1))
    song_url = urls[34]

    req_2 = urllib2.Request(song_url)
    resp_2 = urllib2.urlopen(req_2)
    html_2 = resp_2.read()
    extraction = ""
    for item in html_2.split("</div>"):
       if "<div>" in item:
           extraction = item [ item.find("<div>")+len("<div>") : ]
    extraction = extraction[134:len(extraction)+1]
    r = extraction.replace("<br>", " ")
    elapsed = time.time()-start
    print r
    print "____________________________________________________________________"
    print "Fetched in" , elapsed, "seconds."
    print "\n"
    ask = raw_input("Continue?(Y/N)")
    if ask == "N":
        break
        # not working.
