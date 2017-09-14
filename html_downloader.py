import urllib2

class DownLoad(object):
    def download(self,url):
        if url is None :
            return
        respons = urllib2.urlopen(url)


     print('test')