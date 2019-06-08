
import requests
from urllib.parse import urlencode

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
}
page = 1
base_url = 'https://movie.douban.com/j/new_search_subjects?'

def get_page():
    params = {
        'sort': 'U',
        'range': '0,10',
        'tags': '',
        'start': (page-1)*20,
    }
    url = base_url + urlencode(params)
    try:
        res = requests.get(url, headers=headers)
        if res.status_code == 200:
            return res.json()
    except:
        print("ERROR!")

if __name__ == '__main__':
    while True:
        # 获取页面
        print('正在爬取第%d页...' % page)
        r_movies = get_page()
        for i in r_movies['data']:
            print(i['title'], i['cover'])
        print('第%d页爬取完成' % page)
        c = input('是否爬取下一页y/n:')
        if c.strip().lower() == 'y':
            page += 1
        else:
            print('谢谢使用!')
            break
