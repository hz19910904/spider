
import json
import requests


class DouBan:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
        }
        self.base_url = 'https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=&start={page}'
        self.page = 1

    def get_page(self, url):
        """
        获取页面并提取信息
        :return: 电影信息
        """
        res = requests.get(url, headers=self.headers)
        results = json.loads(res.text)
        return results

    def get_pic_urls(self, r_movies):
        """
        获取图片信息
        :param r_movies: 电影信息
        :return: 图片信息
        """
        pic_urls = []
        r_list = r_movies['data']
        for r_dic in r_list:
            pic_urls.append((r_dic['title'], r_dic['cover']))
        return pic_urls

    def save_msg(self, pic_msgs):
        """
        保存图片到本地
        :param pic_msgs: 图片信息
        :return: none
        """
        for pic_msg in pic_msgs:
            pic_path = './data/%s.jpg' % pic_msg[0]
            pic_url = pic_msg[1]
            res = requests.get(pic_url, headers=self.headers)
            pic_bin = res.content
            with open(pic_path, 'wb') as f:
                f.write(pic_bin)

    def main(self):
        """
        主函数
        :return:none
        """
        while True:
            print("正在爬取第%d页..." % self.page)
            # 得到真实的url
            url = self.base_url.format(page=(self.page-1)*20)
            # 获取页面信息
            r_movies = self.get_page(url)
            # 获取图片地址
            pic_msgs = self.get_pic_urls(r_movies)
            # 保存图片
            self.save_msg(pic_msgs)
            print("第%d页爬取成功！" % self.page)
            c = input("是否爬取下一页（y/n）:")
            if c.strip().lower() == 'y':
                self.page += 1
            else:
                print('谢谢使用！')
                break


if __name__ == '__main__':
    spider = DouBan()
    spider.main()