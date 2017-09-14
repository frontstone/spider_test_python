from test_python import url_manage, html_downloader, html_parser,html_outputer


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manage.UrlManage()
        self.downloader = html_downloader.DownLoad()
        self.parse = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, rootUrl) :
        self.urls.add_new_url(rootUrl)
        count = 1
        while self.urls.has_new_url:
            try:
                new_url = self.urls.get_new_url()
                print(count,new_url)
                html_cont = self.downloader.download()
                new_urls, new_data = self.parse.parse(new_url,html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                count = count + 1
            except:
                print('fail')
        self.outputer.output_html()



if __name__ == "__main__":
    rootUrl =  "https://baike.baidu.com/item/Python/407313?fr=aladdin"
    obj_spider = SpiderMain()
    obj_spider.craw(rootUrl)
