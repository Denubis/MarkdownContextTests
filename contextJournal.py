#!/usr/bin/env python
from __future__ import print_function

from pandocfilters import toJSONFilter, RawInline, Cite, Para, Header, Str, RawBlock, attributes, stringify
import os, sys



"""
Pandoc metadata filter. 

"""

def warning(*objs):
	print("WARNING: ", *objs, file=sys.stderr)

def context(s):
	return RawBlock('context', s)


def myheader(key, value, fmt, meta):			

	if key == 'Header' and fmt == 'context':
		[level, contents, kvs] = value
		if level == 1 and contents == ['title',[],[]]:
			
			z= [context("\chapter{"+stringify(meta['title'])+'}')]+[context("\startlines")]

			
			for line in stringify(meta['author']).split(', '):
				warning(line)
				z.append(context(line))

			z.append(context("\stoplines"))
			return z


if __name__ == "__main__":
	toJSONFilter(myheader)