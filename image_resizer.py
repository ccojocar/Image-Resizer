#!/usr/bin/env python

import os
import sys
import getopt
import glob
import Image

def usage():
    print "Image Resizer\n"
    print "image_resizer.py: [-h] [-d images_folder] [-w width] [-h height]..."
    print ""
    print " -u : help"
    print " -d : path to the image folder"
    print " -w : new image width"
    print " -h : new image height"

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "ud:w:h:", ["help"])
    except getopt.GetoptError, err:
        print str(err)
        usage()
        sys.exit(2)
    width = 640
    height = 480
    path = "/"
    for o, a in opts:
        if o in ("-u", "--help"):
            usage()
            sys.exit()
        if o == "-d":
            path = a          
	if o == "-w":
	    width = int(a)
	if o == "-h":
	    height = int(a)
	    
    resized_path = path + "/resized/"
    listing = os.listdir(path)    
    for infile in listing:
	extension = os.path.splitext(infile)[1]
	if extension in (".jpg", ".jpeg"):
	    print "resizeing: " + infile + "..."
	    im = Image.open(path + "/" + infile)
	    im = im.resize((width, height), Image.ANTIALIAS)
	    if not os.path.exists(resized_path):
		os.makedirs(resized_path)
	    print "saving: " + resized_path + infile + "..." 
	    im.save(resized_path + infile, quality = 100)

if __name__ == "__main__":
    main()
