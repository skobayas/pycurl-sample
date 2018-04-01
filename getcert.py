import pycurl
class getcert(object):
    def __init__(self,fqdn):
        self.client = pycurl.Curl()
        self.client.setopt(pycurl.OPT_CERTINFO, True)
        self.client.setopt(pycurl.URL, "https://" + fqdn)
        self.client.setopt(pycurl.WRITEFUNCTION, lambda x: None)
        self.client.perform()
        self.cert_list = self.client.getinfo(pycurl.INFO_CERTINFO)

    def ee_cert(self):
        return self.cert_list[0][-1][-1].replace("\n", "")

cert_google_com=getcert("google.com")

#print cert_google_com.ee_cert()