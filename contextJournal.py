#!/usr/bin/env python
from __future__ import print_function

from pandocfilters import toJSONFilter, Image, RawInline, Cite, Para, Header, Str, RawBlock, attributes, stringify
import os, sys



"""
Pandoc metadata filter. 

"""

def warning(*objs):
	print("WARNING: ", *objs, file=sys.stderr)

def context(s):
	return RawBlock('context', s)


def myheader(key, value, fmt, meta):			

	if key == 'Image' and fmt == 'context':
		
		warning(value)


if __name__ == "__main__":
	toJSONFilter(myheader)