#!/usr/bin/python
#coding:utf-8
import urllib2
class RedirectHandler(urllib2.HTTPRedirectHandler):
	def http_error_301(self,req,fp,code,msg,headers):
		print '301'
	def http_error_302(self,req,fp,code,msg,headers):
		print '302'