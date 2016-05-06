#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
import mincemeat
import numpy as np
import sys

inp_file = sys.argv[1]
file = open(inp_file,'r')
data = list(file)
file.close()


# The data source can be any dictionary-like object
datasource = dict(enumerate(data))


def mapfn(k, v):
	import hashlib
    	for num in v.split():
		condition = num.isdigit()
		if condition:
     	  		yield 'SUM', int(num)
			yield 'SD', int(num)
			yield 'count', 1

def reducefn(k, vs):
	import numpy as np
	if (k == 'SD'):
		result = np.std(vs)
		return result
	else:
		result = sum(vs)
                return result


s = mincemeat.Server()
s.datasource = dict(enumerate(data))
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")
print results
