#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

import mincemeat


k=range(2,10000001)
def chunks(l,n):
        for i in range(0,len(l),n):
                yield l[i:i+n]
data=chunks(k,5000)

# The data source can be any dictionary-like object
datasource = dict(enumerate(data))


def mapfn(k, v):
	import math
	def isPrime(n):
		if n==2 or n==3 or n==5 or n==7: return True
		if n%2==0 or n<2 or n%3==0 or n%5==0 or n%7==0: return False
		for i in range(11,int(n**0.5)+1,2):   # only odd numbers
			if n%i==0:
		        	return False    
		return True
	for i in range(0,len(v)):
                x=v[i]
                if(str(x) == str(x)[::-1]):
                        num=isPrime(x)
			if num == True:
	                        yield 'Numbers',x
				yield 'SUM',x
				yield 'Count',1
def reducefn(k, vs):
		if (k=='SUM' or k=='Count'):
			return sum(vs)		
                return vs

s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")
print results

