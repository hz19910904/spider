
import requests
import json


class DouBan:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
        }
        self.base_url = 'https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=&start={page}'
        self.page = 1

    def get_page(self, url):
        """
        获取页面信息
        :param url:
        :return:
        """
        res = requests.get(url, headers=self.headers)
        results = json.loads(res.text)
        return results

    def get_pic_url(self, r_movies):
        """
        获取图片信息
        :return:
        """
        pic_msgs = []
        r_list = r_movies['data']
        for r_dic in r_list:
            pic_msgs.append((r_dic['title'], r_dic['cover']))
        return pic_msgs


    def save_msg(self, pic_msgs):
        """
        保存图片到本地
        :return:
        """
        for pic_msg in pic_msgs:
            pic_path = './pictures/%s.jpg' % pic_msg[0]
            pic_url = pic_msg[1]
            res = requests.get(url=pic_url, headers=self.headers)
            with open(pic_path, 'wb') as f:
                f.write(res.content)

    def main(self):
        """
        主函数
        :return:
        """
        while True:
            print("正在爬取第%d页..." % self.page)
            # 得到真实的url地址
            url = self.base_url.format(page=(self.page-1)*20)
            # 获取页面信息
            r_movies = self.get_page(url)
            # 获取图片地址
            pic_msgs = self.get_pic_url(r_movies)
            # 保存图片
            self.save_msg(pic_msgs)
            print("第%d页爬取完成!!!" % self.page)
            c = input("是否爬去下一页y/n:")
            if c.strip().lower() == 'y':
                self.page += 1
            else:
                break


if __name__ == '__main__':
    spider = DouBan()
    spider.main()