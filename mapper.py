#!/usr/bin/env python2
import urllib
import sys
import os

# transformPagename
# input: pagename from dataset
# output: transformPagename -> title}date pageViews
def transformPagename(pagename):
	# 3.1.1 remove percent-encoded
	return urllib.unquote_plus(pagename)

def isValid(page):
	# break down page 
	[code, name, views, size] = page.split(' ')
	# 3.1.2 exclude all non English pages -> project.startsWith("en") == false
	if(code != "en"):
		return False
	# 3.1.3 exlude all pages that start with Media, Special, Talk, User, User_talk, Project, Project_talk, File,File_talk, MediaWiki, MediaWiki_talk, Template, Template_talk, Help, Help_talk, Category, Category_talk, Portal, Wikipedia, or Wikipedia_talk
	invalidStartes = ["Media", "Special", "Talk", "User", "User_talk", "Project", "Project_talk", "File", "File_talk", "MediaWiki", "MediaWiki_talk", "Template", "Template_talk", "Help", "Help_talk", "Category", "Category_talk", "Portal", "Wikipedia", "Wikipedia_talk"]
	for i in invalidStartes:
		if(name.startswith(i)):
			return False
	# 3.1.4 exclude all pages that don't start with a capital letter
	if(name[0].islower()):
		return False
	# 3.1.5 exclude img or txt file extensions -> jpg, gif, .png, .JPG, .GIF, .PNG, .ico, and .txt
	invalidEnder = [".jpg", ".gif", ".png", ".JPG", ".GIF", ".PNG", ".ico", ".txt"]
	for i in invalidEnder:
		if(name.endswith(i)):
			return False
	# 3.1.6 exclude biolerplate pages ->404_error, Main_Page, Hypertext_Transfer_Protocol, Favicon.ico, and Search
	invalidNames = ["404_error", "Main_Page", "Hypertext_Transfer_Protocol", "Favicon.ico", "Search"]
	for i in invalidNames:
		if(name == i):
			return False
	return True

# createOutputString
# input: valid page
# output: title}date pageViews
# def createOutputString(str, day, hour):
# 	page

# mapper
# transforms each pagename and filters out
# input: data
# output: filtered/sorted pagenames
def mapper():
	# print(sys.stdin)
	print(os.readlink('/proc/self/fd/0'))
	data = sys.stdin.readlines()
	# print(data)
	cleaned = map(transformPagename, data)
	# print(cleaned)
	filetered = filter(isValid, cleaned)
	return filtered
	# [pc, day, hour] = filename.split('-')



# sample = ['en Main_Page 242332 4737756101']
# print(mapper(sample))
print(mapper())
