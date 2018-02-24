# coding: utf-8
import pycurl
client=pycurl.Curl()
client.setopt(pycurl.OPT_CERTINFO,True)
client.setopt(pycurl.URL,"https://google.com")
client.perform()
client.getinfo(pycurl.INFO_CERTINFO)
