import pycurl

def getcert(fqdn):
	client=pycurl.Curl()
	client.setopt(pycurl.OPT_CERTINFO,True)
	client.setopt(pycurl.URL,"https://"+fqdn)
	client.setopt(pycurl.WRITEFUNCTION, lambda x: None)
	client.perform()
	cert_list=client.getinfo(pycurl.INFO_CERTINFO)
	return cert_list[0][-1][-1].replace("\n","")

print getcert('google.com')
