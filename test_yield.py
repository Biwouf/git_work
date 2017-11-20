#! /usr/bin/env python3
# coding: utf-8

#Test Yield

def generateur():
	lst = range(3)
	for i in lst:
		yield i*i 

test = generateur()
print(generateur())

for i in test:
	print(i)
