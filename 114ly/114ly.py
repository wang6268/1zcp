#!/usr/bin/env python
#-*- coding:utf-8 -*-
# read the text
txt=open('data.txt','r').read()
txt=txt.lower()
for ch in "~@#$%^&*()_-+=<>?/,.:;{}[]|\'""":
    txt=txt.replace(ch,'')
words=txt.split()


#count the words
counts={}
sumcount=0
for word in words:
    counts[word]=counts.get(word,0)+1
    sumcount=sumcount + 1


print('There are'+str(sumcount) +'words.')
print('They are:')
for word in counts.keys():
    print(word+': '+str(counts[word]))
