import os
import requests
from urllib.parse import urlencode


class DouBan:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
        }
        self.page = 1
        self.base_url = 'https://movie.douban.com/j/new_search_subjects?'

    # 获取电影信息
    def get_page(self):
        params = {
            'sort': 'U',
            'range': '0,10',
            'tags': '',
            'start': (self.page - 1) * 20,
        }
        url = self.base_url + urlencode(params)
        pic_msgs = []
        try:
            res = requests.get(url, headers=self.headers)
            if res.status_code == 200:
                results = res.json()
                for i in results['data']:
                    pic_msgs.append((i['title'], i['cover']))
                return pic_msgs
        except:
            print("ERROR!")

    # 保存图片到本地
    def save_msgs(self, r_movies):
        for pic_msg in r_movies:
            pic_path = './data/%s.jpg' % pic_msg[0]
            pic_url = pic_msg[1]
            res = requests.get(pic_url, headers=self.headers)
            with open(pic_path, 'wb') as f:
                f.write(res.content)

    # 主函数
    def main(self):
        # 创建文件夹./data
        path = './data'
        if not os.path.exists(path):
            os.makedirs(path)
        while True:
            # 获取页面
            print('正在爬取第%d页...' % self.page)
            r_movies = self.get_page()
            # 图片存储
            self.save_msgs(r_movies)
            print('第%d页爬取完成' % self.page)
            c = input('是否爬取下一页y/n:')
            if c.strip().lower() == 'y':
                self.page += 1
            else:
                print('谢谢使用!')
                break


if __name__ == '__main__':
    spider = DouBan()
    spider.main()
