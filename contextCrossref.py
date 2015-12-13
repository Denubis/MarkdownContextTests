#!/usr/bin/env python
from __future__ import print_function

from pandocfilters import toJSONFilter, Table,Image, RawInline, Cite, Para, Header, Str, RawBlock, attributes, stringify
import os, sys, pprint
import re


"""
Pandoc metadata filter. 

"""
def empty(input_list):
    """Recursively iterate through values in nested lists."""
    for item in input_list:
        if not isinstance(item, list) or not empty(item):
             return False
    return True

def alignDict(x):
	return {'AlignLeft':'flushleft',
			'AlignRight':'flushright',
			'AlignCenter':'middle',
			'AlignDefault':'flushleft'}.get(x['t'],0)

def warning(*objs):
	pprint.pprint(*objs, stream=sys.stderr)

def context(s):
	return RawInline('context', s)
def block(s):
	return RawBlock('context', s)

def crossreference(key, value, fmt, meta):			

	if key == 'Image' and fmt == 'context':
		[caption, fig] = value
		
		strCap = re.findall(r'(?:\{(.*)\})? *(.*$)', stringify(caption))
		caption=[RawInline('context',re.sub(r'\{.*\} *', "", stringify(caption)))]
		return [context("\placefigure[here][%s]{%s}{\externalfigure[%s]}" % (strCap[0][0],strCap[0][1],fig[0]))]

	if key == 'Table' and fmt == 'context':
		warning("start")
		warning(value)
		[caption,align,width,head, text] = value
		strCap = re.findall(r'(?:\{(.*)\})? *(.*$)', stringify(caption))

		# todo width
		out = []
		for i, col in enumerate(align):
			out.append(block("\\setupTABLE[column][%s][align={%s,lohi}]" % (i+1,alignDict(col))))			

		out.append(block("\placetable[here][%s]{%s}{" % (strCap[0][0],strCap[0][1])))
		out.append(block("\\bTABLE"))

		if not empty(head):
			out.append(block("\setupTABLE[r][1][background=color,backgroundcolor=gray,style={\\tfa}]"))
			out.append(block("\\bTR"))
			for h in head:
				out.append(block("\\bTH %s \\eTH" % (stringify(h))))
			out.append(block("\\eTR"))
		else:
			out.append(block("\setupTABLE[r][1][background=color,backgroundcolor=white,style={\\tfx}]"))

		for row in text:
			out.append(block("\\bTR"))
			for cell in row:
				out.append(block("\\bTD %s \\eTD" % stringify(cell)))
			out.append(block("\\eTR"))
		out.append(block("\\eTABLE}"))
		
		return out


if __name__ == "__main__":
	toJSONFilter(crossreference)