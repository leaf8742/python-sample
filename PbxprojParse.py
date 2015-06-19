#!/usr/bin/python

'''
Created on 2013-4-23
@author: huji
'''
class stack :
    def __init__( self ):
        self._theItems = list()
    def isEmpty( self ):
        return len( self ) == 0
    def __len__ ( self ):
        return len( self._theItems )
    def peek( self ):
        assert not self.isEmpty(), "Cannot peek at an empty stack"
        return self._theItems[-1]
    def pop( self ):
        assert not self.isEmpty(), "Cannot pop from an empty stack"
        return self._theItems.pop()
    def push( self, item ):
        self._theItems.append( item )
			
def isindict(stacktrace):
	if isinstance(stacktrace.peek(), dict):
		return True
	else:
		return False

def _parse(text):
	sta = stack()
	nodestr=""
	
	for i in range(0,len(text)):
		c=text[i]
		
		if sta.isEmpty():
			sta.push(dict())

		if sta.peek()=="/*":
			if c=="*" and text[i+1] =="/":
				continue
			elif c=="/" and text[i-1] == "*":
				sta.pop()
				continue
			else:
				continue
			
		if sta.peek()=="//":
			if c=="\n":
				sta.pop()
				continue
			else:
				continue
			
		if sta.peek()=="\"":
			if c!="\"":
				nodestr+=c
				continue
			else:
				if text[i-1]=="\\":
					nodestr+=c
					continue
				else:
					sta.pop()
					continue
					
			
		if c=="\n" or c==" " or c=="\t":
			continue

		if c=="{" :
			if nodestr!="":
				sta.push(nodestr)
			sta.push(dict())
			nodestr=""
		elif c=="(":
			if nodestr!="":
				sta.push(nodestr)
			sta.push(list())
			nodestr=""
		elif c=="}" or c==")":
			kvs=None
			ins=sta.pop()
			if isinstance(sta.peek(), str):
				nodestr=sta.pop()
				kvs=nodestr.split("=")
			
			if isindict(sta):
				if kvs!=None:
					key=kvs[0].strip()
					sta.peek()[key]=ins
				else:
					if sta.__len__()==1:
						sta.pop()
						sta.push(ins)
			else:
				sta.peek().append(ins)
			nodestr=None
		else:
			if c=="/" and text[i+1] == "*":
				sta.push("/*")
			elif c=="/" and text[i+1] =="/":
				sta.push("//")
			elif c=="\"":
				sta.push("\"")
			elif c==";" or c==",":
				if nodestr==None:
					nodestr=""
					continue
				else:
					kvs=nodestr.split("=")
					if isindict(sta):
						sta.peek()[kvs[0].strip()]=kvs[1].strip()
					else:
						sta.peek().append(kvs[0].strip())
					nodestr=""
			else:
				nodestr+=c
	return sta.peek()

def parse(text):
	return _parse(text)

def parseFrom(xcodeprojpath):
	pf = open(xcodeprojpath+"/project.pbxproj","r", encoding='utf-8')
	text = pf.read()
	pf.close()
	return parse(text)
